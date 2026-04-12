from src.contexto.contexto import Contexto
from src.servicos.api_youtube.api_youtube import YoutubeAPI
from src.servicos.servico_s3.s3_base import S3Base
from src.corrente.checar_conexao_corrente import ChecarConexaCorrente
from src.operacao_banco.config.db_config_sqlserverlog import \
    DbConfigSQLServerLOG
from src.operacao_banco.operacao.operacao_sql_server import \
    OperacaoSqlServerLOG

from src.utils.log_banco import LogBanco

db_config_log = DbConfigSQLServerLOG()

db_operacao_log = OperacaoSqlServerLOG(conexao=db_config_log)
conexao_s3 = S3Base()

loger = LogBanco(
    db_operacao=db_operacao_log,
    debug="INFO",
    formato_log="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    nome_pacote="main_pipeline",
)

api_youtube = YoutubeAPI(conexao_log=loger)
contexto = Contexto()

config_log = LogBanco(
    db_operacao=db_operacao_log,
    debug="INFO",
    formato_log="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    nome_pacote="main_pipeline",
)


p1 = ChecarConexaCorrente(
    conexao_log=config_log,
    conexao_s3=conexao_s3,
    conexao_youtube=api_youtube,
)


p1.corrente(contexto=contexto)
