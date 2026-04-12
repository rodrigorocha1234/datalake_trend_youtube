from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TConn = TypeVar("TConn")
TDriver = TypeVar("TDriver")


class IDbConfig(ABC, Generic[TConn, TDriver]):

    @abstractmethod
    def obter_driver(self) -> TDriver:
        raise NotImplementedError

    @abstractmethod
    def obter_parametros_conexao(self):
        raise NotImplementedError
