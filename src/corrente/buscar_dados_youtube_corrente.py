from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.utils.Ilog_banco import IlogBanco


class BuscarDadosYoutubeCorrente(Corrente):

    def __init__(self, conexao_log: IlogBanco, youtube_api: IApiYoutube) -> None:
        super().__init__(conexao_log=conexao_log)
        self.__youtube_api = youtube_api

    def executar_processo(self, contexto: Contexto) -> bool:
        dados = self.__youtube_api.obter_video_por_data()
        contexto.gerador_youtube_trend = dados
        return True
