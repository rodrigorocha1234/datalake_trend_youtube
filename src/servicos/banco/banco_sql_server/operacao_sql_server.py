from typing import Any

from src.servicos.banco.config.idb_config import IDbConfig
from src.servicos.banco.interfaces.protocolo import MSSQLConnect


class OperacaoSqlServer:

    def __init__(self, conexao: IDbConfig[MSSQLConnect]):
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

    def salvar_dados(self, **kwargs: Any) -> None:
        sql, param = kwargs["sql"], kwargs["param"]

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
