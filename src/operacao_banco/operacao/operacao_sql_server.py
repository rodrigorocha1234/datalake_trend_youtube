from typing import Any, Tuple

import mssql_python

from src.operacao_banco.config.idb_config import IDbConfig
from src.operacao_banco.config.protocols import MSSQLConnect


class OperacaoSqlServerLOG:

    def __init__(self, conexao: IDbConfig[mssql_python.Connection, MSSQLConnect]):
        self.__conexao = conexao

    def salvar_consulta(self, sql: str, param: Tuple[Any, ...]) -> None:
        driver = self.__conexao.obter_driver()
        args, kwargs = self.__conexao.obter_parametros_conexao()
        con = driver(*args, **kwargs)
        try:
            with con.cursor() as cursor:
                cursor.execute(sql, param)
                con.commit()
        except Exception as e:
            print(e)
        finally:
            con.close()
