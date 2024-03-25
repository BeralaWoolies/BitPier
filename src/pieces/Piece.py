import math
from src.pieces.Block import Block


class Piece:
    def __init__(self, index: int, length: int) -> None:
        self.__index: int = index
        self.__length: int = length
        self.__blocks: list[Block] = self.__initialise_blocks()

    def __initialise_blocks(self) -> list[Block]:
        curr_length: int = self.__length
        blocks: list[Block] = []

        for index in range(math.ceil(curr_length / Block.MAX_LENGTH)):
            blocks.append(Block(index, min(curr_length, Block.MAX_LENGTH)))
            curr_length -= Block.MAX_LENGTH

        return blocks

    def get_index(self) -> int:
        return self.__index

    def __str__(self) -> str:
        info: str = f'piece {self.__index}: {self.__length} bytes\n'
        blocks_length: int = 0
        for block in self.__blocks:
            info += '\t' + str(block)
            blocks_length += block.length
        info += '\t' + f'= {blocks_length} bytes\n'
        return info
