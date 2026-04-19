from abc import ABC, abstractmethod
from typing import Any


class IOperacao(ABC):
    @abstractmethod
    def checar_conexao(self) -> bool:
        pass

    @abstractmethod
    def salvar_dados(self, **kwargs: Any) -> None:
        pass
