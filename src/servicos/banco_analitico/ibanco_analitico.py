from abc import ABC, abstractmethod


class IBancoAnalitico(ABC):

    @abstractmethod
    def checar_conexao(self) -> bool:
        pass
