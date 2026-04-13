import trino

from src.servicos.banco.config.idb_config import IDbConfig
from src.servicos.banco.interfaces.ioperacao import IOperacao
from src.servicos.banco.interfaces.protocolo import TrinoConnect


class OperacaoTrino(IOperacao):

    def __init__(self, configuracao: IDbConfig[trino.dbapi.Connection, TrinoConnect]):
        self.__configuracao = configuracao

    def checar_conexao(self):
        driver = self.__configuracao.obter_driver()
        args, kwargs_conn = self.__configuracao.obter_parametros_conexao()
        host, porta, user, catalog, schema = args[0]
        con = None
        try:
            con = driver(
                host=host,
                port=porta,
                user=user,
                catalog=catalog,
                schema=schema
            )


            with con.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()

            return True

        except Exception as e:
            raise RuntimeError("Falha ao conectar no TRINO") from e

        finally:
            if con:
                con.close()
