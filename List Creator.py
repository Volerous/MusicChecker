from Parser import PlayList
import csv

"""
monstercatFutureBass = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsbRwwi0ode5c9iMQ2dyJU3N')
monstercatDrumBass = PlayList('https://www.youtube.com/playlist?list=PL9BCA60EEB1C8893D')
monstercatElectro = PlayList('https://www.youtube.com/playlist?list=PL21A7A915E7020E73')
monstercatIndieDance = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsZWIBJEqIhsu2VgDI5w7r0d')
monstercatGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsY-hyGZb1POOp8GDdIRng5A')
ncsHouse = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')
ncsDrumBass = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn')
xkitoDrumBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4fZQ5IS-AaTEnsTHy0zuXr8')
xkitoElectro = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dT5siJAyQJag9_-T_X5VT_')
xktioFutureBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4ermdmmjtr6uxYj0eZ_nKc4')
xkitoNuDisco = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4d54-kCbNETZWLO6H1evYrE')
xkitoGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dgellaUrmAcV7s-VhfqHat')
"""

test = PlayList('https://www.youtube.com/playlist?list=PLMC1lL-g1-zajmJpSneZcXCB-dVpMwbcB')
#creates list of clean URLs for use when checking
def makeUrlList(playlistList):
    urlList = []
    for a in playlistList:
        urlList.append(a.url)
    return urlList


#writing to .csv file for saving for the next time
def write(List):
    with open('testOldList.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(List)


#load list from .csv file and creating (# list of strings) from file
def loadList(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        urlList = []
        for row in spamreader:
            str = ', '.join(row)
            urlList.append(str.replace(',',''))
        urlList = list(filter(None,urlList))
        return urlList

#returns a list of all the links to the videoes that aren't in the list(meaning the new videos)
def getDiff(playlistNew, playlistOld):
    List = list(set(playlistNew) - set(playlistOld))
    return List

def getFullList():
    finalList = [item for item in makeUrlList(test.playlist) if not item in loadList('testOldList.csv')]
    finalList = [item for item in makeUrlList(test.playlist) if not item in loadList('testOldList.csv')]
    return finalList
print(getFullList())

"""
monstercatFutureBassOldList = open("monstercatFutureBassOldList.txt", 'w')
monstercatDrumBassOldList = open('monstercatDrumBassOldList.txt', 'w')
monstercatElectroOldList = open('monstercatElectroOldList.txt', 'w')
monstercatGlitchHopOldList = open('monstercatGlitchHopOldList.txt', 'w')
monstercatIndieDanceOldList =
"""