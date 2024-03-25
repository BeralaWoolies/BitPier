import asyncio
from src.protocol.Peer import Peer
from src.protocol.Handshake import Handshake


class PeerConnection:
    def __init__(self, peers: asyncio.Queue, peer_id: bytes, info_hash: bytes) -> None:
        self.__peers: asyncio.Queue = peers
        self.__peer_id: bytes = peer_id
        self.__info_hash: bytes = info_hash
        self.__writer: asyncio.StreamWriter = None
        self.__reader: asyncio.StreamReader = None
        self.__future = asyncio.ensure_future(self.__download())

    async def __download(self) -> None:
        peer: Peer = await self.__peers.get()
        ip: str = peer.ip
        port: int = peer.port

        print(f'Peer Connection assigned with peer: {ip}:{port}')
        self.__reader, self.__writer = await asyncio.open_connection(ip, port)

        buffer = await self.__handshake()

    async def __handshake(self) -> bytes:
        handshake: Handshake = Handshake(self.__peer_id, self.__info_hash)
        self.__writer.write(handshake.encode())
        await self.__writer.drain()

        buffer: bytes = b''
        tries: int = 0
        while len(buffer) < Handshake.LENGTH and tries < 10:
            tries += 1
            buffer = await self.__reader.read(10*1024)

        print(f'Response: {buffer}, {len(buffer)} bytes')
