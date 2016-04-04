from Parser import PlayList
import csv


monstercatFutureBass = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsbRwwi0ode5c9iMQ2dyJU3N')
monstercatDrumBass = PlayList('https://www.youtube.com/playlist?list=PL9BCA60EEB1C8893D')
monstercatElectro = PlayList('https://www.youtube.com/playlist?list=PL21A7A915E7020E73')
monstercatIndieDance = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsZWIBJEqIhsu2VgDI5w7r0d')
monstercatGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsY-hyGZb1POOp8GDdIRng5A')
ncsHouse = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')
ncsDrumBass = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn')
xkitoDrumBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4fZQ5IS-AaTEnsTHy0zuXr8')
xkitoElectro = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dT5siJAyQJag9_-T_X5VT_')
xkitoFutureBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4ermdmmjtr6uxYj0eZ_nKc4')
xkitoNuDisco = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4d54-kCbNETZWLO6H1evYrE')
xkitoGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dgellaUrmAcV7s-VhfqHat')

test = PlayList('https://www.youtube.com/playlist?list=PLMC1lL-g1-zajmJpSneZcXCB-dVpMwbcB')



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

def writeAllLists():
    monstercatElectro.write('monstercatElectroOldList.csv')
    monstercatDrumBass.write('monstercatDrumBassOldList.csv')
    monstercatFutureBass.write('monstercatFutureBassOldList.csv')
    monstercatGlitchHop.write('monstercatGlitchHopOldList.csv')
    monstercatIndieDance.write('monstercatIndieDanceOldList.csv')
    ncsDrumBass.write('ncsDrumBassOldList.csv')
    ncsHouse.write('ncsHouseOldList.csv')
    xkitoDrumBass.write('xkitoDrumBassOldList.csv')
    xkitoElectro.write('xkitoElectroOldList.csv')
    xkitoNuDisco.write('xkitoNuDiscoOldList.csv')
    xkitoGlitchHop.write('xkitoGlitchHopOldList.csv')
    xkitoFutureBass.write('xkitoFutureBassOldList.csv')


def getFullListDiff():
    finalList = [item for item in test.urlList() if not item in loadList('testOldList.csv')]
    finalList.extend([item for item in test.urlList() if not item in loadList('testOldList.csv')])
    return finalList
