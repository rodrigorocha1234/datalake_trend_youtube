import trino

from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.servicos.banco.interfaces.ioperacao import IOperacao

from src.utils.Ilog_banco import IlogBanco


class ChecarConexaCorrente(Corrente):
    def __init__(
            self, conexao_log: IlogBanco, operacao_s3: IOperacao, conexao_youtube: IApiYoutube,
            operacao_trino: IOperacao
    ) -> None:
        super().__init__(conexao_log)
        self.__operacao_s3 = operacao_s3
        self.__conexao_youtube = conexao_youtube
        self.__operacao_trino = operacao_trino

    def executar_processo(self, contexto: Contexto) -> bool:
        s3_ok = self.__operacao_s3.checar_conexao()
        youtube_ok = self.__conexao_youtube.checar_conexao()
        trino_ok = self.__operacao_trino.checar_conexao()

        if s3_ok and youtube_ok and trino_ok:
            self._conexao_log.logger.info(
                f"{self.__class__.__name__} -> Sucesso ao executar todas as conexões (S3, Trino e YouTube)"
            )
            return True

        erros = []

        if not trino_ok:
            erros.append("Trino desconectado")

        if not s3_ok:
            erros.append("S3 desconectado | ")

        if not youtube_ok:
            erros.append("YouTube API desconectada")

        mensagem_erro = (
                f"{self.__class__.__name__} -> Falha de conexão: "
                + " | ".join(erros)
        )

        self._conexao_log.logger.error(mensagem_erro)

        return False
