import numpy as np

sources = [
            #'http://dbpedia.org/resource/Elvis_Presley',
            #'http://dbpedia.org/resource/Wolfgang_Amadeus_Mozart',
            #'http://dbpedia.org/resource/John_Lennon',
            #'http://dbpedia.org/resource/Madonna_%28entertainer%29',
            #'http://dbpedia.org/resource/Richard_Wagner',
            #'http://dbpedia.org/resource/David_Bowie',
            #'http://dbpedia.org/resource/Cher',
            #'http://dbpedia.org/resource/George_Frideric_Handel',
            #'http://dbpedia.org/resource/Ennio_Morricone',
            #'http://dbpedia.org/resource/Andrea_Bocelli',
            #'http://dbpedia.org/resource/Frank_Sinatra',
            #'http://dbpedia.org/resource/Frank_Zappa',
            #'http://dbpedia.org/resource/Freddie_Mercury',
            #'http://dbpedia.org/resource/Johnny_Hallyday',
            #'http://dbpedia.org/resource/Christina_Aguilera',
            #'http://dbpedia.org/resource/Eric_Clapton',
            #'http://dbpedia.org/resource/Britney_Spears',
            #'http://dbpedia.org/resource/John_Williams',
            #'http://dbpedia.org/resource/Mariah_Carey',
            #'http://dbpedia.org/resource/Celine_Dion',
            #'http://dbpedia.org/resource/Jimi_Hendrix',
            'http://dbpedia.org/resource/George_Harrison',
            'http://dbpedia.org/resource/Miles_Davis',
            'http://dbpedia.org/resource/Kylie_Minogue',
            'http://dbpedia.org/resource/Felix_Mendelssohn',
            'http://dbpedia.org/resource/Snoop_Dogg',
            'http://dbpedia.org/resource/Neil_Young',
            'http://dbpedia.org/resource/Serge_Gainsbourg',
            'http://dbpedia.org/resource/Antonio_Vivaldi',
            'http://dbpedia.org/resource/Avril_Lavigne',
            'http://dbpedia.org/resource/Dolly_Parton',
            'http://dbpedia.org/resource/Giuseppe_Verdi',
            'http://dbpedia.org/resource/Joan_Baez',
            'http://dbpedia.org/resource/Cyndi_Lauper',
            'http://dbpedia.org/resource/Jerry_Goldsmith',
            'http://dbpedia.org/resource/Jean_Michel_Jarre',
            'http://dbpedia.org/resource/Barbra_Streisand',
            'http://dbpedia.org/resource/Janet_Jackson',
            'http://dbpedia.org/resource/Bruce_Springsteen',
            'http://dbpedia.org/resource/Ringo_Starr',
            'http://dbpedia.org/resource/Tom_Waits',
            'http://dbpedia.org/resource/Rihanna',
            'http://dbpedia.org/resource/James_Brown',
            'http://dbpedia.org/resource/Jimmy_Page',
            'http://dbpedia.org/resource/Igor_Stravinsky',
            'http://dbpedia.org/resource/Kanye_West',
            'http://dbpedia.org/resource/Stevie_Wonder',
            'http://dbpedia.org/resource/Mike_Oldfield',
            'http://dbpedia.org/resource/Kurt_Cobain',
            'http://dbpedia.org/resource/Henry_Mancini',
            'http://dbpedia.org/resource/Alice_Cooper',
            'http://dbpedia.org/resource/Tupac_Shakur',
            'http://dbpedia.org/resource/Phil_Collins',
            'http://dbpedia.org/resource/Jennifer_Lopez',
            'http://dbpedia.org/resource/Bo_Diddley',
            'http://dbpedia.org/resource/Roger_Waters',
            'http://dbpedia.org/resource/Ozzy_Osbourne',
            'http://dbpedia.org/resource/Hans_Zimmer',
            'http://dbpedia.org/resource/Pete_Townshend',
            'http://dbpedia.org/resource/Karlheinz_Stockhausen',
            'http://dbpedia.org/resource/Alicia_Keys',
            'http://dbpedia.org/resource/Justin_Timberlake',
            'http://dbpedia.org/resource/Tina_Turner',
            'http://dbpedia.org/resource/Louis_Armstrong',
            'http://dbpedia.org/resource/Brian_May',
            'http://dbpedia.org/resource/Georges_Brassens',
            'http://dbpedia.org/resource/Nelly_Furtado',
            'http://dbpedia.org/resource/Van_Morrison',
            'http://dbpedia.org/resource/Yoko_Ono',
            'http://dbpedia.org/resource/Amy_Winehouse',
            'http://dbpedia.org/resource/Solomon_Burke',
            'http://dbpedia.org/resource/Bing_Crosby',
            'http://dbpedia.org/resource/Whitney_Houston',
            'http://dbpedia.org/resource/Claude_Debussy',
            'http://dbpedia.org/resource/Philip_Glass',
            'http://dbpedia.org/resource/Alanis_Morissette',
            'http://dbpedia.org/resource/George_Michael',
            'http://dbpedia.org/resource/Patti_Smith',
            'http://dbpedia.org/resource/Iggy_Pop',
            'http://dbpedia.org/resource/Robbie_Williams',
            'http://dbpedia.org/resource/Gwen_Stefani',
            'http://dbpedia.org/resource/Charles_Aznavour',
            'http://dbpedia.org/resource/David_Gilmour',
            'http://dbpedia.org/resource/Captain_Beefheart',
            'http://dbpedia.org/resource/Tarja_Turunen',
            'http://dbpedia.org/resource/Ayumi_Hamasaki',
            'http://dbpedia.org/resource/Bryan_Adams',
            'http://dbpedia.org/resource/Arnold_Schoenberg',
            'http://dbpedia.org/resource/Carl_Stalling',
            'http://dbpedia.org/resource/Renaud',
            'http://dbpedia.org/resource/Dean_Martin',
            'http://dbpedia.org/resource/Shania_Twain',
            'http://dbpedia.org/resource/Enrique_Iglesias',
            'http://dbpedia.org/resource/Marvin_Gaye',
            'http://dbpedia.org/resource/Ashley_Tisdale',
            'http://dbpedia.org/resource/Duke_Ellington',
            'http://dbpedia.org/resource/Diana_Ross'
        ]

destinations = [
            'http://dbpedia.org/resource/Germany',
            'http://dbpedia.org/resource/Spain',
            'http://dbpedia.org/resource/China',
            'http://dbpedia.org/resource/San_Francisco',
            'http://dbpedia.org/resource/Rio_de_Janeiro',
            'http://dbpedia.org/resource/New_York',
            'http://dbpedia.org/resource/Paris',
            'http://dbpedia.org/resource/Germany',
            'http://dbpedia.org/resource/Chile',
            'http://dbpedia.org/resource/India',
            'http://dbpedia.org/resource/Brazil',
            'http://dbpedia.org/resource/Iran',
            'http://dbpedia.org/resource/Italy',
            'http://dbpedia.org/resource/Japan',
            'http://dbpedia.org/resource/Netherlands',
            'http://dbpedia.org/resource/Chicago',
            'http://dbpedia.org/resource/Hungary',
            'http://dbpedia.org/resource/London',
            'http://dbpedia.org/resource/Los_Angeles',
            'http://dbpedia.org/resource/Belgium',
            'http://dbpedia.org/resource/Algeria',
            'http://dbpedia.org/resource/Lisbon',
            'http://dbpedia.org/resource/Greece',
            'http://dbpedia.org/resource/Iceland',
            'http://dbpedia.org/resource/Bulgaria',
            'http://dbpedia.org/resource/Colombia',
            'http://dbpedia.org/resource/California',
            'http://dbpedia.org/resource/Morocco',
            'http://dbpedia.org/resource/Berlin',
            'http://dbpedia.org/resource/Norway',
            'http://dbpedia.org/resource/Moscow',
            'http://dbpedia.org/resource/European_Union',
            'http://dbpedia.org/resource/Finland',
            'http://dbpedia.org/resource/Europe',
            'http://dbpedia.org/resource/Republic_of_Ireland',
            'http://dbpedia.org/resource/Barcelona',
            'http://dbpedia.org/resource/Croatia',
            'http://dbpedia.org/resource/England',
            'http://dbpedia.org/resource/Kazakhstan',
            'http://dbpedia.org/resource/Amsterdam',
            'http://dbpedia.org/resource/Athens',
            'http://dbpedia.org/resource/Cairo',
            'http://dbpedia.org/resource/Cleveland',
            'http://dbpedia.org/resource/Burma',
            'http://dbpedia.org/resource/Alaska',
            'http://dbpedia.org/resource/Elvis_Presley',
            'http://dbpedia.org/resource/Wolfgang_Amadeus_Mozart',
            'http://dbpedia.org/resource/John_Lennon',
            'http://dbpedia.org/resource/Richard_Wagner',
            'http://dbpedia.org/resource/David_Bowie',
            'http://dbpedia.org/resource/Cher',
            'http://dbpedia.org/resource/George_Frideric_Handel',
            'http://dbpedia.org/resource/Ennio_Morricone',
            'http://dbpedia.org/resource/Andrea_Bocelli',
            'http://dbpedia.org/resource/Frank_Sinatra',
            'http://dbpedia.org/resource/Frank_Zappa',
            'http://dbpedia.org/resource/Freddie_Mercury',
            'http://dbpedia.org/resource/Johnny_Hallyday',
            'http://dbpedia.org/resource/Christina_Aguilera',
            'http://dbpedia.org/resource/Eric_Clapton',
            'http://dbpedia.org/resource/Britney_Spears',
            'http://dbpedia.org/resource/John_Williams',
            'http://dbpedia.org/resource/Mariah_Carey',
            'http://dbpedia.org/resource/Celine_Dion',
            'http://dbpedia.org/resource/Jimi_Hendrix',
            'http://dbpedia.org/resource/George_Harrison',
            'http://dbpedia.org/resource/Miles_Davis',
            'http://dbpedia.org/resource/Kylie_Minogue',
            'http://dbpedia.org/resource/Felix_Mendelssohn',
            'http://dbpedia.org/resource/Snoop_Dogg',
            'http://dbpedia.org/resource/Neil_Young',
            'http://dbpedia.org/resource/Serge_Gainsbourg',
            'http://dbpedia.org/resource/Antonio_Vivaldi',
            'http://dbpedia.org/resource/Avril_Lavigne',
            'http://dbpedia.org/resource/Dolly_Parton',
            'http://dbpedia.org/resource/Giuseppe_Verdi',
            'http://dbpedia.org/resource/Joan_Baez',
            'http://dbpedia.org/resource/Cyndi_Lauper',
            'http://dbpedia.org/resource/Jerry_Goldsmith',
            'http://dbpedia.org/resource/Jean_Michel_Jarre',
            'http://dbpedia.org/resource/Barbra_Streisand',
            'http://dbpedia.org/resource/Janet_Jackson',
            'http://dbpedia.org/resource/Bruce_Springsteen',
            'http://dbpedia.org/resource/Ringo_Starr',
            'http://dbpedia.org/resource/Tom_Waits',
            'http://dbpedia.org/resource/Rihanna',
            'http://dbpedia.org/resource/James_Brown',
            'http://dbpedia.org/resource/Jimmy_Page',
            'http://dbpedia.org/resource/Igor_Stravinsky',
            'http://dbpedia.org/resource/Kanye_West',
            'http://dbpedia.org/resource/Stevie_Wonder',
            'http://dbpedia.org/resource/Mike_Oldfield',
            'http://dbpedia.org/resource/Kurt_Cobain',
            'http://dbpedia.org/resource/Henry_Mancini',
            'http://dbpedia.org/resource/Alice_Cooper',
            'http://dbpedia.org/resource/Tupac_Shakur',
            'http://dbpedia.org/resource/Phil_Collins'
]

def randomSourceAndDestination():
    response = dict()
    random_source = np.random.randint(len(sources))
    random_dest = np.random.randint(len(destinations))
    response['source'] = sources[random_source]
    response['destination'] = destinations[random_dest]
    return response
