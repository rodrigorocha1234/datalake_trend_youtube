from typing import Any, Dict, Tuple, Type

from minio.api import Minio

from src.config.config import Config
from src.servicos.banco.config.idb_config import IDbConfig


class ConfigS3Minio(IDbConfig):
    def obter_driver(self) -> Type[Minio]:
        return Minio

    def obter_parametros_conexao(self) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
        conn_str = (
            Config.HOST_TRINO,
            Config.PORT_TRINO,
            Config.USER_TRINO
        )

        return ((conn_str,), {})

