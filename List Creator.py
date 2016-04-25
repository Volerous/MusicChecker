from Parser import PlayList
import os


monstercatFutureBass = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsbRwwi0ode5c9iMQ2dyJU3N', 'mcFB')
monstercatDrumBass = PlayList('https://www.youtube.com/playlist?list=PL9BCA60EEB1C8893D', 'mcDB')
monstercatElectro = PlayList('https://www.youtube.com/playlist?list=PL21A7A915E7020E73', 'mcElectro')
monstercatIndieDance = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsZWIBJEqIhsu2VgDI5w7r0d', 'mcID')
monstercatGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLe8jmEHFkvsY-hyGZb1POOp8GDdIRng5A', 'mcGH')
ncsHouse = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK', 'ncsHouse')
ncsDrumBass = PlayList('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn', 'ncsDB')
xkitoDrumBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4fZQ5IS-AaTEnsTHy0zuXr8', 'xkitoDB')
xkitoElectro = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dT5siJAyQJag9_-T_X5VT_', 'xkitoElectro')
xkitoFutureBass = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4ermdmmjtr6uxYj0eZ_nKc4', 'xkitoFB')
xkitoNuDisco = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4d54-kCbNETZWLO6H1evYrE', 'xkitoND')
xkitoGlitchHop = PlayList('https://www.youtube.com/playlist?list=PLvlw_ICcAI4dgellaUrmAcV7s-VhfqHat', 'xkitoGH')


def writeAllLists():
    monstercatElectro.write()
    monstercatDrumBass.write()
    monstercatFutureBass.write()
    monstercatGlitchHop.write()
    monstercatIndieDance.write()
    ncsDrumBass.write()
    ncsHouse.write()
    xkitoDrumBass.write()
    xkitoElectro.write()
    xkitoNuDisco.write()
    xkitoGlitchHop.write()
    xkitoFutureBass.write()


def getFullListDiff():
    finalList = []
    finalList.extend(monstercatElectro.diff())
    finalList.extend(monstercatIndieDance.diff())
    finalList.extend(monstercatGlitchHop.diff())
    finalList.extend(monstercatDrumBass.diff())
    finalList.extend(monstercatFutureBass.diff())
    finalList.extend(ncsHouse.diff())
    finalList.extend(ncsDrumBass.diff())
    finalList.extend(xkitoDrumBass.diff())
    finalList.extend(xkitoGlitchHop.diff())
    finalList.extend(xkitoElectro.diff())
    finalList.extend(xkitoNuDisco.diff())
    finalList.extend(xkitoFutureBass.diff())
    return finalList


for a in getFullListDiff():
    os.system('youtube-dl -x --audio-format mp3 -o "%%(uploader)s-%%(title)s-%%(id)s.%%(ext)s" %s' % a)
writeAllLists()