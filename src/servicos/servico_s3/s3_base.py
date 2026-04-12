import socket

from src.config.config import Config
from src.servicos.servico_s3.is3_base import IS3Base


class S3Base(IS3Base):
    def __init__(self) -> None:
        self.__host = Config.HOST_S3
        self.__port = int(Config.PORT_S3)

    def checar_conexao(self) -> bool:
        try:
            with socket.create_connection((self.__host, self.__port), timeout=10):
                return True
        except OSError:
            return False
