from typing import Any, Protocol

import mssql_python
from minio import Minio


class MSSQLConnect(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> mssql_python.Connection:
        ...


class MinioConnect(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> Minio:
        ...
