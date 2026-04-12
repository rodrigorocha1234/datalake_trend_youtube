from abc import ABC, abstractmethod


class IS3Base(ABC):

    @abstractmethod
    def checar_conexao(self) -> bool:
        pass
