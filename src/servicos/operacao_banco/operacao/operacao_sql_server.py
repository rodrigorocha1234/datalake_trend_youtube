from typing import Any, Tuple

import mssql_python

from src.servicos.operacao_banco.config.idb_config import IDbConfig
from src.servicos.operacao_banco.config.protocols import MSSQLConnect


class OperacaoSqlServer:

    def __init__(self, conexao: IDbConfig[mssql_python.Connection, MSSQLConnect]):
        self.__conexao = conexao

    def checar_conexao(self) -> bool:
        driver = self.__conexao.obter_driver()
        args, kwargs_conn = self.__conexao.obter_parametros_conexao()

        con = None
        try:
            con = driver(*args, **kwargs_conn)

            with con.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()

            return True

        except Exception as e:
            raise RuntimeError("Falha ao conectar no SQL Server") from e

        finally:
            if con:
                con.close()

    def salvar_dados(self, dado: Tuple[str, Tuple[Any, ...]], **kwargs: Any) -> None:
        sql, param = dado

        driver = self.__conexao.obter_driver()
        args, kwargs_conn = self.__conexao.obter_parametros_conexao()

        con = driver(*args, **kwargs_conn)

        try:
            with con.cursor() as cursor:
                cursor.execute(sql, param)
                con.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao executar SQL: {sql}") from e
        finally:
            con.close()
