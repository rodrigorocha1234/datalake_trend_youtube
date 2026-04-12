from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class IOperacao(Protocol):

    def checar_conexao(self) -> bool:
        ...

    def salvar_dados(self,  **kwargs: Any) -> None:
        pass