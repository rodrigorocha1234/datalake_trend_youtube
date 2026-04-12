from typing import Protocol, TypeVar

TConn = TypeVar("TConn", covariant=True)


class ConnectCallable(Protocol[TConn]):
    def __call__(self, conn_str: str) -> TConn: ...
