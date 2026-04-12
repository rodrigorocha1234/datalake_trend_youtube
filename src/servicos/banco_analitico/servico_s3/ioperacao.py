from typing import Protocol, TypeVar, Generic, Any, runtime_checkable


T = TypeVar("T", contravariant=True)


@runtime_checkable
class IOperacao(Protocol, Generic[T]):
    def salvar_dados(self, dado: T, **kwargs: Any) -> None:
        ...
