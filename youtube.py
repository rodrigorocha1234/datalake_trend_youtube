from datetime import datetime

from src.servicos.api_youtube.api_youtube import YoutubeAPI
from src.servicos.operacao_banco.config.db_config_sqlserverlog import \
    DbConfigSQLServerLOG
from src.utils.log_sql_server import LogBancoSQLServer

db_config_log = DbConfigSQLServerLOG()

config_log = LogBancoSQLServer(
    configuracao_conexao=db_config_log,
    debug="INFO",
    formato_log="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    nome_pacote="main_pipeline",
)

youtube_api = YoutubeAPI(conexao_log=config_log)

dados = youtube_api.obter_video_por_data(
    data_inicio=datetime.now(),
)

for dado in dados:
    print(dado)

