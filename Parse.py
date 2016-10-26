from ListCreator import *
parser = argparse.ArgumentParser(prog='')
parser.add_argument('-f','--full', help='Full run of the playlists and download', action='store_const',const=dlSongs)
parser.add_argument('-s','--song', help='download song with the settings',action='store_const', const=dl)
parser.add_argument('-d','--date', help='Download song before or after date',action='store_const', const=dlSongsDate)
args = parser.parse_args()
