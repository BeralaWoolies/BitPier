import aiohttp
import random
import asyncio
import urllib.parse
from src.TorrentFile import TorrentFile
from src.responses.TrackerResponse import TrackerResponse
from src.protocol.PeerConnection import PeerConnection
from src.pieces.PieceManager import PieceManager

MAX_PEER_CONNECTIONS = 50


class TorrentClient:
    def __init__(self, path: str, port: int) -> None:
        self.__torrent: TorrentFile = TorrentFile(path)
        self.__port: int = port
        self.__peer_id: bytes = random.randbytes(20)
        self.__peers: asyncio.Queue = asyncio.Queue()
        self.__peer_connections: list[PeerConnection] = []
        self.__piece_manager: PieceManager = PieceManager(self.__torrent)

    async def start(self) -> None:
        print(self.__torrent)
        print(f'Peer Id: {self.__peer_id}')
        print(self.__piece_manager)

        print('\nContacting tracker...')
        tracker_res: TrackerResponse = await self.__contact_tracker()
        print(tracker_res)

        for peer in tracker_res.peers:
            self.__peers.put_nowait(peer)

        self.__peer_connections = [PeerConnection(self.__peers,
                                                  self.__peer_id,
                                                  self.__torrent.info_hash)
                                   for _ in range(MAX_PEER_CONNECTIONS)]
        while True:
            await asyncio.sleep(5)

    async def __contact_tracker(self) -> TrackerResponse:
        async with aiohttp.ClientSession() as session:
            params = {
                'info_hash': self.__torrent.info_hash,
                'peer_id': self.__peer_id,
                'port': self.__port,
                'uploaded': 0,
                'downloaded': 0,
                'left': self.__torrent.length,
                'compact': 1,
            }

            async with session.get(self.__torrent.announce + '?' + urllib.parse.urlencode(params)) as res:
                if not res.status == 200:
                    raise ConnectionError('Unable to connect to tracker')
                data = await res.read()
                return TrackerResponse(data)
