class Block:
    MAX_LENGTH = 2**14

    def __init__(self, index: int, length: int) -> None:
        self.__index: int = index
        self.__length: int = length
        self.__data: bytes = None

    @property
    def length(self) -> int:
        return self.__length

    def __str__(self) -> str:
        return f'block {self.__index}: {self.__length} bytes\n'
