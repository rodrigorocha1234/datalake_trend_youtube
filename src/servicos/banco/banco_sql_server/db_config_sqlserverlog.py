from typing import Any, Dict, Tuple

import mssql_python

from src.config.config import Config
from src.servicos.banco.config.idb_config import IDbConfig
from src.servicos.banco.interfaces.protocolo import MSSQLConnect


class DbConfigSQLServerLOG(
    IDbConfig
):

    def obter_driver(self) -> MSSQLConnect:
        return mssql_python.connect

    def obter_parametros_conexao(self) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
        conn_str = (
            f"Server={Config.HOST_LOG},{Config.PORT_LOG};"
            f"Database={Config.DB_LOG};"
            f"Uid={Config.USER_LOG};"
            f"Pwd={Config.PASSWORD_LOG};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )


        return ((conn_str,), {})
