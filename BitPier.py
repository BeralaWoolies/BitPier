import argparse
import asyncio
import sys
from src.TorrentClient import TorrentClient

# Constants
PORT = 6881

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('torrent', help='The path to a torrent file to download (e.g file.torrent)')
args = parser.parse_args()

# start client
client: TorrentClient = TorrentClient(args.torrent, PORT)

# run client
try:
    asyncio.run(client.start())
except ConnectionError as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)