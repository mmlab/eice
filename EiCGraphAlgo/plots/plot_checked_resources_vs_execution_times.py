from core import cached_pathfinder
import sys, time
import scipy.stats as spst
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy.random import normal
from pylab import *
from scipy.stats import gaussian_kde

def violin_plot(ax,data,pos, bp=False):
    '''
    create violin plots on an axis
    '''
    dist = max(pos)-min(pos)
    w = min(0.15*max(dist,1.0),0.5)
    for d,p in zip(data,pos):
        k = gaussian_kde(d) #calculates the kernel density
        m = k.dataset.min() #lower bound of violin
        M = k.dataset.max() #upper bound of violin
        x = arange(m,M,(M-m)/100.) # support for violin
        v = k.evaluate(x) #violin profile (density curve)
        v = v/v.max()*w #scaling the violin to the available space
        ax.fill_betweenx(x,p,v+p,facecolor='b',alpha=0.2)
        ax.fill_betweenx(x,p,-v+p,facecolor='b',alpha=0.2)
    if bp:
        ax.boxplot(data,notch=0,positions=pos,vert=1, whis=1)

def plot(cpf = cached_pathfinder.CachedPathFinder()):
    total_paths = cpf.loadStoredPaths(max=None)
    #print(total_paths)
    #print(cpf.path_execution_times)
    
    x = list()
    y = list()
    topop = set()
    for checked_resources in cpf.path_execution_time_by_checked_resources:
        if len(cpf.path_execution_time_by_checked_resources[checked_resources]) > 1:
            for execution_time in cpf.path_execution_time_by_checked_resources[checked_resources]:
                x.append(checked_resources)
                y.append(execution_time)
        else:
            topop.add(checked_resources)
    
    for pop in topop:
        cpf.path_execution_time_by_checked_resources.pop(pop)    
             
    #print (x)
    #print (y)
    
    fig = Figure(figsize=(7,6))
    
    # Create a canvas and add the figure to it.
    canvas = FigureCanvas(fig)
    
    # Create a subplot.
    ax = fig.add_subplot(111)
    
    # Set the title.
    ax.set_title('Execution time in function of checked resources (n = %s)' % total_paths,fontsize=12)
    
    # Set the X Axis label.
    ax.set_xlabel('(#) Checked resources',fontsize=9)
    
    # Set the Y Axis label.
    ax.set_ylabel('Execution time (ms)',fontsize=9)
    
    #ax.set_yscale('log')
    
    ax.set_ylim([0,(np.int(np.max(y)/10000)+1)*10000])
    ax.set_xlim([0,(np.int(np.max(x))+1)])
    
    # Display Grid.
    ax.grid(True,linestyle='-',color='0.75')
    
    
    x_n = np.array(x)
    y_n = np.array(y)
    
    m,b = np.polyfit(x_n, y_n, 1)
    #print (m,b) 

    # Generate the Scatter Plot.
    ax.scatter(x,y,s=3,color='tomato')
    ax.plot(x_n, m*x_n+b, '-', alpha=0.7) 
    
#    datas = list()
#    w = 0.5
#    
#    for item in cpf.path_execution_time_by_checked_resources:
#        sorted = np.sort(cpf.path_execution_time_by_checked_resources[item])
#        spread = sorted
#        center = ones(len(sorted)) * np.median(sorted)
#        data = concatenate((spread, center), 0)
#        data.shape = (-1, 1)
#        datas.append(data)
    
    #violin_plot(ax,list(cpf.path_execution_time_by_checked_resources.values()),range(1,len(cpf.path_execution_time_by_checked_resources)+1),bp=True)
        
    # Making a 2-D array only works if all the columns are the
    # same length.  If they are not, then use a list instead.
    # This is actually more efficient because boxplot converts
    # a 2-D array into a list of vectors internally anyway.
    # multiple box plots on one figure
    # ax.boxplot(datas,0,'rx',1,1.99)
    
    
    try:
        path = "/tmp/scatter_{0}_{1}.png".format(hash(time.time()),np.random.randint(10000))
        canvas.print_figure(path)
    except:
        #print (sys.exc_info())
        pass
    return path