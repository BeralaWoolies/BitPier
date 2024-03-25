import argparse
import asyncio
import sys
from src.TorrentClient import TorrentClient

# Constants
PORT = 6881


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'torrent', help='The path to a torrent file to download (e.g file.torrent)')
    return parser.parse_args()


def main():
    # parse command line arguments
    args = parse_arguments()

    # start clients
    client: TorrentClient = TorrentClient(args.torrent, PORT)

    # run client
    try:
        asyncio.run(client.start())
    except KeyboardInterrupt as e:
        print('Quitting gracefully')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
    finally:
        sys.exit(1)


if __name__ == "__main__":
    main()
