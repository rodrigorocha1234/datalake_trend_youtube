import trino

from src.servicos.banco.config.idb_config import IDbConfig
from src.servicos.banco.interfaces.protocolo import TrinoConnect


class DbConfigTrino(IDbConfig):
    def obter_driver(self) -> TrinoConnect:
        return trino.dbapi.connect

    def obter_parametros_conexao(self):
        pass
