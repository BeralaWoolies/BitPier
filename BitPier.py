import argparse
from src.TorrentFile import TorrentFile

parser = argparse.ArgumentParser()
parser.add_argument('torrent', help='The path to a torrent file to download (e.g file.torrent)')

args = parser.parse_args()

torrent = TorrentFile(args.torrent)

torrent.print_info()