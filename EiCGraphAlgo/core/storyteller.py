import numpy as np
import networkx as nx
from core import resourceretriever, graph
import time, gc, sys, logging
from core.worker_pool import Worker

logger = logging.getLogger('pathFinder')
query_log = logging.getLogger('query')

class Storyteller:
    """This class contains the adjecency matrix and provides interfaces to interact with it.
    Besides the adjacency matrix it also holds the fetched resources in a hash set.
    """
    resources = dict()
    resources_by_parent = dict()
    set_definitions = dict()
    iteration = 0

    def __init__(self,s1,s2,threshold=1.1):
        """Initialization of all required containers"""
        self.worker = Worker()
        self.resources = dict()
        self.resources_by_parent = dict()   
        self.storedResources = dict()  
        self.initMatrix(s1, s2)
        self.threshold = threshold
        self.checked_resources = 0
        
        
    def initMatrix(self, source1, source2):
        """Initialization of the adjacency matrix based on input source and destination."""
        query_log.info('Path between {0} and {1}'.format(source1,source2))
        s1 = '<%s>' % source1
        s2 = '<%s>' % source2
        self.resources[0] = s1
        self.resources[1] = s2
        self.stateGraph = np.zeros((2, 2), np.byte)
        self.stateGraph[0] = [1, 0]
        self.stateGraph[1] = [0, 1]
        self.iteration += 1
        return self.stateGraph

    def iterateMatrix(self, blacklist=set()):
        """Iteration phase,
        During this phase the children of the current bottom level nodes are fetched and added to the hashed set.
        
        **Parameters**
    
        blacklist : set, optional (default = empty)
            list of resources to exclude from the pathfinding algorithm
    
        **Returns**
        
        response : stateGraph
            contains the updated adjacency matrix after fetching new resources
        """
        logger.info ('--- NEW ITERATION ---')
        logger.info ('Existing resources {0}'.format(str(len(self.resources))))
        logger.info ('Indexed resources by parents {0}'.format(str(len(self.resources_by_parent))))
        logger.info ('Grandmother: {0}'.format(self.resources[0]))
        logger.info ('Grandfather: {0}'.format(self.resources[1]))
        logger.info ('--- --- ---')
        
        start = time.clock()
        additionalResources = set()
        prevResources = set()
        
        for key in self.resources:
            prevResources.add(self.resources[key])
            
        self.worker.startQueue(resourceretriever.fetchResource, num_of_threads=32)
            
        for resource in prevResources:
            item = [resource, self.resources_by_parent, additionalResources, blacklist]
            self.worker.queueFunction(resourceretriever.fetchResource, item)
        
        self.worker.waitforFunctionsFinish(resourceretriever.fetchResource)
        
        toAddResources = list(additionalResources - prevResources)    
        #toAddResources = filter(resourceretriever.isResource, toAddResources)
        
        gc.collect()
        
        logger.info('Updated indexed resources with parents {0}'.format(str(len(self.resources_by_parent))))    
        
        n = len(self.resources)
        
        for resource in toAddResources:
            self.resources[n] = resource
            n = n + 1
            
        logger.info ('Total resources: %s' % str(n))
        
        self.checked_resources += len(additionalResources)
            
        halt1 = time.clock()
        logger.info ('resource gathering: %s' % str(halt1 - start))
        self.stateGraph = np.zeros(shape=(n, n), dtype=np.byte)
        
        [self.buildGraph(i, n) for i in range(n)]
        halt2 = time.clock()
        logger.info ('graph construction: %s' % str(halt2 - halt1))
        
        #For next iteration, e.g. if no path was found
        #Check for singular values to reduce dimensions of existing resources
        self.storedResources.update(self.resources)
        
        if not graph.pathExists(self.stateGraph) and self.iteration > 1:
            try:
                logger.info ('reducing matrix')
                logger.debug (len(self.stateGraph))
                k = np.int((1-np.divide(1,self.iteration))*250)
                h = (nx.pagerank_scipy(nx.Graph(self.stateGraph), max_iter=100, tol=1e-07))
                #h = (nx.hits_scipy(nx.Graph(self.stateGraph), max_iter=100, tol=1e-07))
                res = list(sorted(h, key=h.__getitem__, reverse=True))
                logger.debug(k)
                
                #u, s, vt = scipy.linalg.svd(self.stateGraph.astype('float32'), full_matrices=False)
                
                
                #rank = resourceretriever.rankToKeep(u, s, self.threshold)
                #unimportant resources are unlikely to provide a path
                #unimportant = resourceretriever.unimportantResources(u, rank, s)
                #important = resourceretriever.importantResources(u, rank)

                #print ('error ratio:')                
                #print (np.divide(len(unimportant & important)*100,len(important)))
                unimportant = res[k:]
                self.resources = resourceretriever.removeUnimportantResources(unimportant, self.resources)            
                halt3 = time.clock()
                logger.info ('rank reducing: %s' % str(halt3 - halt2))
                logger.info('Updated resources amount: %s' % str(len(self.resources)))
            except:
                logger.error ('Graph is empty')
                logger.error (sys.exc_info())
        
        logger.info ('total %s' % str(time.clock()-start))
        logger.info ('=== === ===')
        self.iteration+=1
        return self.resources
    
    def generateDescriptor(self,resource):
        S = set()
        resource = '<%s>' % resource.strip('<>')
        for parent in self.resources_by_parent[resource]:
            link = self.resources_by_parent[resource][parent]
            if link['inverse']:
                pass
                key = self.generateSetHash(link['uri'],resource)
            else:
                key = self.generateSetHash(link['uri'],parent)
            S.add(key)

        return S

    
    def generateSetHash(self,predicate,obj):
        return hash('%s_%s' % (predicate,obj))
    
    class SetDefinition:
        predicate = ""
        obj = ""
        
        def __str__(self):
            return '%s %s' % (self.predicate, self.obj)
    
    def getObjectSets(self):
        S = dict()
        for target in self.resources_by_parent:
            for source in self.resources_by_parent[target]:
                link = self.resources_by_parent[target][source]
                definition = self.SetDefinition()
                definition.predicate = link['uri']
                if link['inverse']:
                    key = self.generateSetHash(link['uri'],target)
                    if not key in S:
                        S[key] = set()
                        self.set_definitions[key] = definition
                    
                    S[key].add(source)
                    definition.obj = target
                    
                else:
                    key = self.generateSetHash(link['uri'],source)
                    if not key in S:
                        S[key] = set()
                        self.set_definitions[key] = definition
                    definition.obj = source
                    S[key].add(target)
        print (self.resources_by_parent)             
        return S
    
    def buildGraph(self, i, n):
        """Builds a graph based on row number i and size n"""
        row = np.zeros(n, np.byte)
        [self.matchResource(i, j, row) for j in range(n)]
        self.stateGraph[i] = row
        
    def matchResource(self, i, j, row):
        """Matches each resource with row and column number i and j in a row from the adjacency matrix"""
        try:
            if i == j:
                row[j] = 1
            elif not self.resources[j] in self.resources_by_parent:
                row[j] = 0
            elif i in self.resources:
                if self.resources[i] in self.resources_by_parent[self.resources[j]]:
                    row[j] = 1
                else:
                    row[j] = 0
            else:
                row[j] = 0
        
        except:
            row[j] = 0
            logger.error ('error %s not found in list of resources' % str(j))
            logger.error (self.resources)
            logger.error (sys.exc_info())
            
    
    def resourceFetcher(self):
        q = self.worker.getQueue(self.resourceFetcher)
        while True:
            item = q.get()
            resourceretriever.fetchResource(item[0], item[1], item[2], item[3])
            q.task_done()
                
    def getResourcesByParent(self):
        return self.resources_by_parent
     
    def getGraph(self):
        return self.stateGraph    
    
    def getResources(self):
        return self.storedResources
