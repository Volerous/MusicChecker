from Parser import PlayList
import os
import argparse

playlistNames = ['Monstercat - Future Bass',
                 'Monstercat - Drum & Bass',
                 'Monstercat - Electro',
                 'Monstercat - Indie Dance',
                 'Monstercat - Glitch Hop',
                 'Monstercat - House',
                 'NCS - House',
                 'NCS - Drum & Bass',
                 'xKito - Drum & Bass',
                 'xKito - Electro',
                 'xKito - Future Bass',
                 'xKito - Nu Disco',
                 'xKito - Glitch Hop',
                 'Vexento - Electro',
                 'Vexento - Inspiration',
                 'Vexento - Chill',
                 'Artzie Music']
urlList = ['https://www.youtube.com/playlist?list=PLe8jmEHFkvsbRwwi0ode5c9iMQ2dyJU3N',
           'https://www.youtube.com/playlist?list=PL9BCA60EEB1C8893D',
           'https://www.youtube.com/playlist?list=PL21A7A915E7020E73',
           'https://www.youtube.com/playlist?list=PLe8jmEHFkvsZWIBJEqIhsu2VgDI5w7r0d',
           'https://www.youtube.com/playlist?list=PLe8jmEHFkvsY-hyGZb1POOp8GDdIRng5A',
           'https://www.youtube.com/playlist?list=PLDF056FBA2E172F87',
           'https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK',
           'https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4fZQ5IS-AaTEnsTHy0zuXr8',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4dT5siJAyQJag9_-T_X5VT_',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4ermdmmjtr6uxYj0eZ_nKc4',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4d54-kCbNETZWLO6H1evYrE',
           'https://www.youtube.com/playlist?list=PLvlw_ICcAI4dgellaUrmAcV7s-VhfqHat',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMCo1PBgnOGjbA6V6AhCb2nB',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMDKfLXUHv9a5nUAU2ogqn42',
           'https://www.youtube.com/playlist?list=PLcd3emSF7UMCEVznCb2foDghKoq7ehcD1',
           'https://www.youtube.com/playlist?list=PLWvkIZpd20Tyq9xOXW9qb_lcZ7TSbVGpa']

def createPlaylists():
    playlist = []
    for a,b in zip(playlistNames,urlList):
        z = PlayList(b,a)
        playlist.append(z)
    return playlist

playlists = createPlaylists()

def writeAllLists():
    for a in playlists:
        a.write()

def getFullListDiff():
    finalList = []
    for a in playlists:
        finalList += a.diff()
    return finalList

def createFiles():
    for a in playlists:
        if not os.path.isfile(a.fileName):
            a.writeE()

def dlSongs():
    for a in playlists:
        for song in a.diff():
            print("%s" % song)
        for song in a.diff():
            os.system('youtube-dl -x -i --audio-format mp3 -o "%s - %%(title)s-%%(id)s.%%(ext)s" %s' %
                  (a.name, song))


def dlSongsDate(date):
    for a in playlists:
        os.system('youtube-dl -x --audio-format mp3 -i --dateafter %s -o "%s - %%(title)s-%%(id)s.%%(ext)s" %s' %
                  (date,a.name, a.listURL))

def updateCSVFiles():
    for a in playlists:
        a.updateCSVFile()

def pickle():
    for a in playlists:
        a.write()

def test_pickle():
    for a in playlists:
        print(a.oldList())
        print(a.diff())

def dl(list):
    os.system('youtube-dl -x -i --audio-format mp3 %s' % list)
dlSongs()
pickle()