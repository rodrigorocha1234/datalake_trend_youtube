from datetime import datetime
from typing import Dict, Generator

from googleapiclient.discovery import build  # type: ignore

from src.config.config import Config
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.utils.log_banco import LogBanco


class YoutubeAPI(IApiYoutube):

    def __init__(self, conexao_log: LogBanco):
        self.__youtube = build(
            'youtube', 'v3', developerKey=Config.CHAVE_API_YOUTUBE)
        self.__conexao_log = conexao_log

    def checar_conexao(self) -> bool:
        try:
            self.__youtube.videos().list(
                part="statistics,contentDetails,snippet",
                chart="mostPopular",
                maxResults=50,
                regionCode="BR",
                key=Config.CHAVE_API_YOUTUBE
            ).execute()
            return True
        except Exception as e:
            self.__conexao_log.loger.error('Erro ao conectar com a API do YouTube', extra={
                "descricao": "Erro ao conectar com a API do YouTube",
                "url": 'url Vídeo',
                "codigo": 500,
                'requisicao': e
            })
            return False

    def obter_video_por_data(self, data_inicio: datetime) -> Generator[Dict, None, None]:

        data_inicio_string = data_inicio.strftime("%Y-%m-%dT%H:%M:%SZ")
        flag_token = True
        token = ''

        while flag_token:
            request = self.__youtube.search().list(
                part="statistics,contentDetails,id,snippet,status, localizations, topicDetails",
                regionCode="BR",
                chart="mostPopular",
                publishedAfter=data_inicio_string,
                pageToken=token,
                maxResults=50

            )

            response = request.execute()

            self.__conexao_log.loger.info('Sucesso ao recuperar playlist', extra={
                "descricao": "Consulta vídeo YouTube",
                "url": 'url Vídeo',
                "codigo": 200,
                'requisicao': response
            })

            try:
                yield from response['items']
                token = response['nextPageToken']
                flag_token = True
            except KeyError:
                flag_token = False
