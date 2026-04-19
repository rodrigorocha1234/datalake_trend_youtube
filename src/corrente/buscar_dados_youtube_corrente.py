from src.contexto.contexto import Contexto
from src.corrente.corrente import Corrente
from src.utils.Ilog_banco import IlogBanco


class BuscarDadosYoutubeCorrente(Corrente):

    def __init__(self, conexao_log: IlogBanco) -> None:
        super().__init__(conexao_log=conexao_log)


    def executar_processo(self, contexto: Contexto) -> bool:
        pass
