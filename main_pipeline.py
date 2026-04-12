

from src.corrente.checar_conexao_corrente import ChecarConexaCorrente
from src.servicos.operacao_banco.config.db_config_sqlserverlog import \
    DbConfigSQLServerLOG
from src.contexto.contexto import Contexto

from src.servicos.api_youtube.api_youtube import YoutubeAPI
from src.servicos.banco_analitico.servico_s3.db_config_minio import \
    ConfigS3Minio
from src.servicos.banco_analitico.servico_s3.operacao_minio_s3 import \
    OperacaoMInioS3
from src.utils.log_sql_server import LogBancoSQLServer

db_config_log = DbConfigSQLServerLOG()


configuracao_s3 = ConfigS3Minio()
operacao_s3 = OperacaoMInioS3(conexao_s3=configuracao_s3)


config_log = LogBancoSQLServer(
    configuracao_conexao=db_config_log,
    debug="INFO",
    formato_log="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    nome_pacote="main_pipeline",
)


api_youtube = YoutubeAPI(conexao_log=config_log)

contexto = Contexto()
p1 = ChecarConexaCorrente(
    conexao_log=config_log,
    operacao_s3=operacao_s3,
    conexao_youtube=api_youtube,
)


p1.corrente(contexto=contexto)
