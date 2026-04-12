from typing import Protocol
import logging


class IlogBanco(Protocol):
    @property
    def logger(self) -> logging.Logger:
        ...
