

class Peer:
    def __init__(self, ip: str, port: int) -> None:
        self.__ip = ip
        self.__port = port

    def print_info(self) -> None:
        print(f'IP: {self.__ip}, PORT: {self.__port}')