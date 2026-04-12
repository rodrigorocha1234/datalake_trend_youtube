
import logging
from abc import ABC, abstractmethod


class IlogBanco(logging.Handler, ABC):

    @abstractmethod
    def emit(self, record: logging.LogRecord) -> None:
        pass
