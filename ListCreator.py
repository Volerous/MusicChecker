from Parser import PlayList
import os

playlistNames = ['Monstercat - Future Bass',
                 'Monstercat - Drum & Bass',
                 'Monstercat - Electro',
                 'Monstercat - Indie Dance',
                 'Monstercat - Glitch Hop',
                 'NCS - House',
                 'NCS - Drum & Bass',
                 'xKito - Drum & Bass',
                 'xKito - Electro',
                 'xKito - Future Bass',
                 'xKito - Nu Disco',
                 'xKito - Glitch Hop',
                 'Nihon Media Network - Jazz',
                 'Nihon Media Network - Denpa',
                 'Nihon Media Network - Electronic',
                 'Nihon Media Network - Kawaii',
                 'Nihon Media Network - Rap',
                 'Nihon Media Network - House',
                 'Nihon Media Network - Drum & Bass',
                 'Nihon Media Network - Future Bass',
                 'Vexento - Electro',
                 'Vexento - Inspiration',
                 'Vexento - Chill']
urlList = ['https://www.youtube.com/playlist?list=PLe8jmEHFkvsbRwwi0ode5c9iMQ2dyJU3N',
           'https://www.youtube.com/playlist?list=PL9BCA60EEB1C8893D',
           'https://www.youtube.com/playlist?list=PL21A7A915E7020E73',
           'https://www.youtube.com/playlist?list=PLe8jmEHFkvsZWIBJEqIhsu2VgDI5w7r0d',
           'https://www.youtube.com/playlist?list=PLe8jmEHFkvsY-hyGZb1POOp8GDdIRng5A',
           'https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK',
           'https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4fZQ5IS-AaTEnsTHy0zuXr8',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4dT5siJAyQJag9_-T_X5VT_',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4ermdmmjtr6uxYj0eZ_nKc4',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4d54-kCbNETZWLO6H1evYrE',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4dgellaUrmAcV7s-VhfqHat',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKd1p3PGOHeEnrvcSQU_Q9H1',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKcx7D7lcpfPbnmSXzg5Af95',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKddZ2WNYPChlArP4E0Umn5g',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKdP_v08ouP5P6W_RKq2P-fq',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKdrReAGw02sy1yauy89MLNx',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKeZQj443X9z2ZEyO561Yww7',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKfn2u6GkCaSpVzr0EfM1_vQ',
           'https://www.youtube.com/playlist?list=PLhj_RADGYLKd-qvJnKL3-FlAp1907EWZB',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMCo1PBgnOGjbA6V6AhCb2nB',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMDKfLXUHv9a5nUAU2ogqn42',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMCEVznCb2foDghKoq7ehcD1']

playlists = []
for a,b in zip(playlistNames,urlList):
    a = PlayList(b,a)
    playlists.append(a)

def writeAllLists():
    for a in playlists:
        a.write()

def getFullListDiff():
    finalList = []
    for a in playlists:
        finalList += a.diff()
    return finalList

def createFile():
    for a in playlists:
        if not os.path.isfile(a.fileName):
            a.writeE()

def dlSongs():
    for a in playlists:
        for song in a.diff():
            os.system('youtube-dl -x --audio-format mp3 -o "%s - %%(title)s-%%(id)s.%%(ext)s" %s' % (a.name, song))

def updateCSVFiles():
    for a in playlists:
        a.updateCSVFile()
updateCSVFiles()