

from datetime import datetime
from typing import Dict, Generator

from googleapiclient.discovery import build  # type: ignore

from src.config.config import Config
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.utils.Ilog_banco import IlogBanco


class YoutubeAPI(IApiYoutube):

    def __init__(self, conexao_log: IlogBanco):

        self.__youtube = build(
            'youtube', 'v3', developerKey=Config.CHAVE_API_YOUTUBE)
        self.__conexao_log = conexao_log

    def checar_conexao(self) -> bool:
        try:
            self.__youtube.videos().list(
                part="statistics,contentDetails,snippet",
                chart="mostPopular",
                regionCode="BR",  # Brasil
                maxResults=50,

                key=Config.CHAVE_API_YOUTUBE
            ).execute()
            return True
        except Exception as e:
            self.__conexao_log.logger.error('Erro ao conectar com a API do YouTube', )
            return False

    def obter_video_por_data(self) -> Generator[Dict, None, None]:

        flag_token = True
        token = ''

        while flag_token:
            request = self.__youtube.videos().list(
                part="statistics,contentDetails,id,snippet,status, localizations, topicDetails",
                regionCode="BR",
                chart="mostPopular",
                pageToken=token,
                maxResults=50

            )

            response = request.execute()

            self.__conexao_log.logger.info('Sucesso ao recuperar playlist', extra={
                'status_code': 200,
                'requisicao': response
            })

            try:
                yield from response['items']
                token = response['nextPageToken']
                flag_token = True
            except KeyError:
                flag_token = False
