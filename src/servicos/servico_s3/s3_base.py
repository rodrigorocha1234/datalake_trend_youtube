import socket

from src.config.config import Config
from src.servicos.banco_analitico.ibanco import IBanco


class S3Base(IBanco):
    def __init__(self) -> None:
        self.__host = Config.HOST_S3
        self.__port = int(Config.PORT_S3)

    def checar_conexao(self) -> bool:
        try:
            with socket.create_connection((self.__host, self.__port), timeout=10):
                return True
        except OSError:
            return False
