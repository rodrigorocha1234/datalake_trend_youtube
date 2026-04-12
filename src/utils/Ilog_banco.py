# interface
from typing import Protocol, runtime_checkable
import logging


@runtime_checkable
class IlogBanco(Protocol):
    @property
    def logger(self) -> logging.Logger:
        ...
