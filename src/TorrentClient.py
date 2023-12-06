from src.TorrentFile import TorrentFile
from src.responses.TrackerResponse import TrackerResponse
import aiohttp
import random
import urllib.parse

class TorrentClient:
    def __init__(self, path: str, port: int) -> None:
        self.__torrent: TorrentFile = TorrentFile(path)
        self.__port: int = port

    async def start(self) -> None:
        self.__torrent.print_info()

        print('\nContacting tracker...')
        tracker_res: TrackerResponse = await self.__contact_tracker()
        tracker_res.print_info()

    async def __contact_tracker(self) -> TrackerResponse:
        async with aiohttp.ClientSession() as session:
            params = {
                'info_hash': self.__torrent.get_info_hash(),
                'peer_id': random.randbytes(20),
                'port': self.__port,
                'uploaded': 0,
                'downloaded': 0,
                'left': self.__torrent.get_length(),
                'compact': 1,
            }

            async with session.get(self.__torrent.get_announce() + '?' + urllib.parse.urlencode(params)) as res:
                if not res.status == 200:
                    raise ConnectionError('Unable to connect to tracker')
                data = await res.read()
                return TrackerResponse(data)
