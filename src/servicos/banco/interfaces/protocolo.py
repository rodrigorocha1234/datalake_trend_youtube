from typing import Protocol, Any, Callable
import mssql_python
import trino
from minio.api import Minio

MSSQLConnect = Callable[..., mssql_python.Connection]
TrinoConnect = Callable[..., trino.dbapi.Connection]
MinioConnect = Callable[..., Minio]