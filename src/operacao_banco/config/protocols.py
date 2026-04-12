from typing import Protocol, Any
import mssql_python


class MSSQLConnect(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> mssql_python.Connection:
        ...
