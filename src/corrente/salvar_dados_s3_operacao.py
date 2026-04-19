from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.servicos.api_youtube.iapi_youtube import IApiYoutube
from src.servicos.banco.interfaces.ioperacao import IOperacao
from src.utils.Ilog_banco import IlogBanco


class SalvarDadosS3(Corrente):

    def __init__(self, conexao_log: IlogBanco, operacao_s3: IOperacao) -> None:
        super().__init__(conexao_log=conexao_log)
        self.__operacao_s3 = operacao_s3

    def executar_processo(self, contexto: Contexto) -> bool:
       return True