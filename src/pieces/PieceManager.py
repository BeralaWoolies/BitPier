import math
from src.TorrentFile import TorrentFile
from src.pieces.Piece import Piece


class PieceManager:
    def __init__(self, torrent: TorrentFile) -> None:
        self.__torrent: TorrentFile = torrent
        self.__pieces: list[Piece] = self.__initialise_pieces()

    def __initialise_pieces(self) -> list[Piece]:
        curr_length: int = self.__torrent.length
        piece_length: int = self.__torrent.piece_length
        pieces: list[Piece] = []

        for index in range(math.ceil(curr_length / piece_length)):
            pieces.append(Piece(index, min(curr_length, piece_length)))
            curr_length -= piece_length

        return pieces

    def __str__(self) -> str:
        info: str = 'Pieces: \n'
        for piece in self.__pieces:
            info += str(piece)
        return info
