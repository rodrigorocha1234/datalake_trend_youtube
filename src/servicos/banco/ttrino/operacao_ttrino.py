

from src.servicos.operacao_banco.config.idb_config import IDbConfig


class OperacaoTrino:

    def __init__(self, configuracao: IDbConfig):
        self.__configuracao = configuracao

    def checar_conexao(self):
        driver = self.__configuracao.obter_driver()
        args, kwargs_conn = self.__configuracao.obter_parametros_conexao()

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