from abc import abstractmethod

from src.servicos.banco_analitico.ibanco_analitico import IBancoAnalitico


class IS3Base(IBancoAnalitico):

    @abstractmethod
    def checar_conexao(self) -> bool:
        pass
