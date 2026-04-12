from typing import Any, Dict, Tuple, Type

from minio.api import Minio

from src.config.config import Config
from src.servicos.banco.config.idb_config import IDbConfig


class ConfigS3Minio(IDbConfig):
    def obter_driver(self) -> Type[Minio]:
        return Minio

    def obter_parametros_conexao(self) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
        conn_str = (
            Config.HOST_S3,
            Config.PORT_S3,
            Config.USER_S3,
            Config.PASSWORD_S3
        )

        return ((conn_str,), {})

#   def checar_conexao(self) -> bool:
#        try:
#             with socket.create_connection((self.__host, self.__port), timeout=10):
#                 return True
#         except OSError:
#             return False
