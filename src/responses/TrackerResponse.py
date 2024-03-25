import bencodepy
from src.protocol.Peer import Peer


class TrackerResponse:
    def __init__(self, encoded_data: bytes) -> None:
        self.__decode_response(encoded_data)

    def __decode_response(self, encoded_data: bytes) -> None:
        decoded_data: dict = bencodepy.decode(encoded_data)
        self.__interval: int = decoded_data.get(b'interval', 0)

        peers: bytes = decoded_data.get(b'peers', b'')
        split_peers: list[bytes] = [peers[i:i+6]
                                    for i in range(0, len(peers), 6)]
        peer_components: list[tuple[bytes, bytes]] = [
            (peer[:4], peer[4:]) for peer in split_peers]

        self.__peers: list[Peer] = [Peer('.'.join(map(str, ip_bytes)), int.from_bytes(port_bytes, byteorder='big'))
                                    for ip_bytes, port_bytes in peer_components]

    @property
    def peers(self) -> list[Peer]:
        return self.__peers

    def __str__(self) -> str:
        info: str = 'Tracker response: \n'
        info += f'Interval: {self.__interval} seconds\n'
        info += f'Peers: \n'
        for peer in self.__peers:
            info += str(peer)
        return info
