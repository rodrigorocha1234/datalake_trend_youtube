from typing import Protocol, Tuple, Any


class IOperacao(Protocol):
    def salvar_dados(self, sql: str, param: Tuple[Any, ...]) -> None:
        ...
