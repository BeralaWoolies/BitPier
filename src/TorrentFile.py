import bencodepy
import hashlib


class TorrentFile:
    def __init__(self, path: str) -> None:
        self.__decode_torrent(path)

    def __decode_torrent(self, path: str) -> None:
        with open(path, 'rb') as torrent_file:
            decoded_data: dict = bencodepy.decode(torrent_file.read())
            self.__announce: str = decoded_data.get(b'announce', b'').decode()
            self.__creation_date: int = decoded_data.get(b'creation date', 0)

            info: dict = decoded_data.get(b'info', {})
            self.__length: int = info.get(b'length', 0)
            self.__name: str = info.get(b'name', b'').decode()
            self.__piece_length: int = info.get(b'piece length', 0)
            self.__info_hash: bytes = hashlib.sha1(
                bencodepy.encode(info)).digest()

            pieces: bytes = info[b'pieces']
            self.__piece_hashes: list[bytes] = [pieces[i:i+20]
                                                for i in range(0, len(pieces), 20)]

    @property
    def info_hash(self) -> bytes:
        return self.__info_hash

    @property
    def length(self) -> int:
        return self.__length

    @property
    def announce(self) -> str:
        return self.__announce

    @property
    def piece_length(self) -> str:
        return self.__piece_length

    def __str__(self) -> str:
        info: str = 'Torrent Info:\n'
        info += f'Name: {self.__name}\n'
        info += f'Announce url: {self.__announce}\n'
        info += f'Creation date: {self.__creation_date}\n'
        info += f'Length: {self.__length} bytes\n'
        info += f'Piece length: {self.__piece_length} bytes\n'
        info += f'Info hash: {self.__info_hash}'
        return info
