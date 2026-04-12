from typing import Protocol, Tuple, Any, runtime_checkable


@runtime_checkable
class IOperacao(Protocol):

    def checar_conexao(self) -> bool:
        ...

    def salvar_dados(self, **kwargs) -> None:
        ...
