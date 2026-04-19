from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.servicos.banco.interfaces.ioperacao import IOperacao
from src.utils.Ilog_banco import IlogBanco


class SalvarDadosS3(Corrente):

    def __init__(self, conexao_log: IlogBanco, operacao_s3: IOperacao) -> None:
        super().__init__(conexao_log=conexao_log)
        self.__operacao_s3 = operacao_s3

    def __salvar_dados_s3(self, contexto: Contexto) -> bool:
        try:
            dados_youtube = contexto.gerador_youtube_trend
            for dado in dados_youtube:
                self.__operacao_s3.salvar_dados(dado=dado)
            return True
        except Exception:
            return False

    def executar_processo(self, contexto: Contexto) -> bool:

        return True
