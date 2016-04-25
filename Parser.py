from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import csv

"""This class extracts the urls and titles of a given youtube playlist"""

class PlayList:
	# name tuple to store outputs
    Video = namedtuple('Video', ['url', 'title'])

    def __init__(self, listurl, name):
        self.name = name
        # get the html text
        self.__listurl = self.__makeUrl(listurl)
        htmldoc = requests.get(self.__listurl).text
        # parse the html
        soup = BeautifulSoup(htmldoc, 'html.parser')
        # get all the pl(aylist)-video-title-link(s):
        rawList = soup('a', {'class' : 'pl-video-title-link'})
        # there has to be at least 1 item in a playlist
        if len(rawList) < 1:
            raise ValueError('This might be either a private ' \
                              'or an empty playlist.')
        else:
            # list of the raw hrefs and their anchor texts
            self.__rawList = [(x.get('href'), x.contents[0].strip())
                              for x in rawList]
        self.urlList = self.__urlList()
        self.fileName = 'csv files/' + self.name + '.csv'

    @property
    def playlist(self):
		# return the playlist as a list of named tuples
        return [PlayList.Video._make([self.__getVideoURL(x[0])] + [x[1]])
                for x in self.__rawList]

    def __getVideoURL(self, text):
		# helper function split extract url and add prefix
        url = text.split('&')[0]
        url = 'https://www.youtube.com' + url
        return url

    def __makeUrl(self, text):
		# url validation and clean up
        if text.find('playlist?list') != -1:
            return text
        elif text.find('watch?v=') * text.find('list=') > 1:
            return self.__getListUrlfromVideoLink(text)
        else:
            raise ValueError('Playlist ID not found in URL.')


    def __getListUrlfromVideoLink(self, text):
		# helper function as its name implies
        return r'''https://www.youtube.com/playlist?''' + \
               [x for x in text.split('&')
                if x.startswith('list=')][0]

    # creates list of clean URLs for use when checking
    def __urlList(self):
        urlList = []
        for a in self.playlist:
            urlList.append(a.url)
        return urlList

    # writing to .csv file for saving for the next time
    def write(self):
        with open(self.fileName, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.urlList)

    # load list from .csv file and creating (# list of strings) from file
    def oldList(self):
        with open(self.fileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            urlList = []
            for row in spamreader:
                str = ', '.join(row)
                urlList.append(str.replace(',', ''))
            urlList = list(filter(None, urlList))
            return urlList
    def diff(self):
        return [item for item in self.urlList if not item in self.oldList()]