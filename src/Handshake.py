NUM_RESERVED_BYTES = 8
PSTR_LEN = b'\x13'
PSTR = b'BitTorrent protocol'

class Handshake:
    def __init__(self, peer_id: bytes, info_hash: bytes) -> None:
        self.__peer_id: bytes = peer_id
        self.__info_hash: bytes = info_hash
        self.__length: int = len(PSTR_LEN) + len(PSTR) + NUM_RESERVED_BYTES + len(info_hash) + len(peer_id)

    def encode(self) -> bytes:
        buffer = PSTR_LEN + PSTR + b'\x00' * NUM_RESERVED_BYTES
        buffer += self.__info_hash
        buffer += self.__peer_id
        return buffer

    def get_length(self) -> int:
        return self.__length