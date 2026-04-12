import trino

from src.config.config import Config
from src.servicos.banco.config.idb_config import IDbConfig
from src.servicos.banco.interfaces.protocolo import TrinoConnect


class DbConfigTrino(IDbConfig):
    def obter_driver(self) -> TrinoConnect:
        return trino.dbapi.connect

    def obter_parametros_conexao(self):
        conn_str = (
            Config.HOST_TRINO,
            Config.PORT_TRINO,
            Config.USER_TRINO,
            Config.CATALOG_TRINO,
            Config.SCHEMA_TRINO,
        )
        return ((conn_str,), {})
