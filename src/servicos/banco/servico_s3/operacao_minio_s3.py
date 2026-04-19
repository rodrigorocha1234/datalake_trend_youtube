import socket
from typing import Any

from src.config.config import Config
from src.servicos.banco.config.idb_config import IDbConfig


class OperacaoMInioS3:
    def __init__(self, conexao_s3: IDbConfig):
        self.__conexao_s3 = conexao_s3
        self.__host = Config.HOST_S3
        self.__port = int(Config.PORT_S3)

    def checar_conexao(self) -> bool:
        try:
            with socket.create_connection((self.__host, self.__port), timeout=10):
                return True
        except OSError:
            return False

    def salvar_dados(self, **kwargs: Any) -> None:
        pass