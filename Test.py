from Parser import *
from ListCreator import *
import os
import cProfile

test = PlayList('https://www.youtube.com/playlist?list=PLMC1lL-g1-zajmJpSneZcXCB-dVpMwbcB','Test Playlist')
s = "test = PlayList('https://www.youtube.com/playlist?list=PLMC1lL-g1-zajmJpSneZcXCB-dVpMwbcB','Test Playlist')"
print("Tests For %s" % test.fileName)

#urlList
testList = ['https://www.youtube.com/watch?v=SeyweGHLxSg','https://www.youtube.com/watch?v=yappQQtfk8Q']
if testList == test.urlList:
    print("test for urlList: %s" % str(True))
else:
    print("test for urlList: %s" % str(False))

#empty file
test.writeE()
if os.stat(test.fileName).st_size == 0:
    print('test for empty file: %s' % True)
else:
    print('test for empty file %s' % False)

#fileName
print("Test for fileName:")
if test.fileName == 'csv files/Test Playlist.csv':
    print("%s" % True)
else:
    print("%s" % False)

#FileWrite
test.write(test.urlList)

#oldList()
print("%s" % (test.oldList[0]))
print("%s" % (test.urlList))
test.write(test.urlList)
print(test.oldList)
print(test.urlList)
a = [s for s in test.oldList if "=" in s]
b = list(filter(lambda x: 'watch' in x, test.oldList))
any('=' == x for x in test.oldList)
print(a)
print(b)

#Timing of Functions
