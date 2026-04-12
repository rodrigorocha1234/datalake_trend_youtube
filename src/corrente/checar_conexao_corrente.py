from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.servicos.banco_analitico.ibanco import IBanco
from src.utils.Ilog_banco import IlogBanco


class ChecarConexaCorrente(Corrente):
    def __init__(self, conexao_log: IlogBanco, conexao_s3: IBanco, conexao_youtube: IApiYoutube) -> None:
        super().__init__(conexao_log)
        self.__conexao_s3 = conexao_s3
        self.__conexao_youtube = conexao_youtube

    def executar_processo(self, contexto: Contexto) -> bool:
        s3_ok = self.__conexao_s3.checar_conexao()
        youtube_ok = self.__conexao_youtube.checar_conexao()

        if s3_ok and youtube_ok:
            self._conexao_log.info(
                f"{self.__class__.__name__} -> Sucesso ao executar todas as conexões (S3 e YouTube)"
            )
            return True

        erros = []

        if not s3_ok:
            erros.append("S3 desconectado | ")

        if not youtube_ok:
            erros.append("YouTube API desconectada")

        mensagem_erro = (
            f"{self.__class__.__name__} -> Falha de conexão: "
            + " | ".join(erros)
        )

        self._conexao_log.loger.error(mensagem_erro)

        return False
