from typing import Protocol, Tuple, Any


class IOperacao(Protocol):
    def salvar_consulta(self, sql: str, param: Tuple[Any, ...]) -> None:
        ...
