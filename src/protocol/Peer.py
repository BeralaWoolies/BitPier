class Peer:
    def __init__(self, ip: str, port: int) -> None:
        self.__ip = ip
        self.__port = port

    @property
    def ip(self) -> str:
        return self.__ip

    @property
    def port(self) -> int:
        return self.__port

    def __str__(self) -> str:
        return f'IP: {self.__ip}, PORT: {self.__port}\n'
