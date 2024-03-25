NUM_RESERVED_BYTES = 8
PSTR_LEN = b'\x13'
PSTR = b'BitTorrent protocol'


class Handshake:
    # peer_id and info_hash are both 20 bytes each
    LENGTH = len(PSTR_LEN) + len(PSTR) + NUM_RESERVED_BYTES + 40

    def __init__(self, peer_id: bytes, info_hash: bytes) -> None:
        self.__peer_id: bytes = peer_id
        self.__info_hash: bytes = info_hash

    def encode(self) -> bytes:
        return b''.join([
            PSTR_LEN,
            PSTR,
            b'\x00' * NUM_RESERVED_BYTES,
            self.__info_hash,
            self.__peer_id
        ])
