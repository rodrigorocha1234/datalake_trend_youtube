import socket
from typing import TypeVar

from src.operacao_banco.config.idb_config import IDbConfig

TConn = TypeVar("TConn")
TDriver = TypeVar("TDriver")


class S3Base(IDbConfig[TConn, TDriver]):

    def obter_driver(self) -> TDriver:
        raise NotImplementedError

    def obter_parametros_conexao(self):
        raise NotImplementedError


#   def checar_conexao(self) -> bool:
#        try:
#             with socket.create_connection((self.__host, self.__port), timeout=10):
#                 return True
#         except OSError:
#             return False
