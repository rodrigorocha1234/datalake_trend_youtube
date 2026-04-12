from abc import ABC, abstractmethod


class IBanco(ABC):

    @abstractmethod
    def checar_conexao(self) -> bool:
        pass
