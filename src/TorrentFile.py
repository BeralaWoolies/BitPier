import bencodepy
import hashlib
from datetime import datetime

class TorrentFile:
    def __init__(self, torrent_path: str) -> None:
        self.__decode_torrent(torrent_path)

    def __decode_torrent(self, torrent_path: str) -> None:
        with open(torrent_path, 'rb') as torrent_file:
            decoded_dict = bencodepy.decode(torrent_file.read())
            self.__announce = decoded_dict.get(b'announce', b'').decode()
            self.__creation_date = decoded_dict.get(b'creation date', 0)

            info_dict = decoded_dict.get(b'info', {})
            self.__length = info_dict.get(b'length', 0)
            self.__name = info_dict.get(b'name', b'').decode()
            self.__piece_length = info_dict.get(b'piece length', 0)
            self.__info_hash = hashlib.sha1(bencodepy.encode(info_dict)).digest()

            pieces = info_dict[b'pieces']
            self.__piece_hashes = [pieces[i:i+20] for i in range(0, len(pieces), 20)]

    def print_info(self) -> None:
        print('Torrent Info:')
        print(f'Name: {self.__name}')
        print(f'Announce url: {self.__announce}')
        print(f'Creation date: {self.__creation_date} | {datetime.fromtimestamp(self.__creation_date)}')
        print(f'Length: {self.__length} bytes')
        print(f'Piece length: {self.__piece_length} bytes')
        print(f'Info hash: {self.__info_hash}')
