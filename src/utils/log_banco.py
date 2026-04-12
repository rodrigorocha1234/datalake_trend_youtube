
import logging
from abc import ABC, abstractmethod
from typing import Literal

from src.operacao_banco.config.idb_config import IDbConfig


class LogBanco(logging.Handler, ABC):
    def __init__(
        self,
        configuracao_conexao: IDbConfig,
        debug: Literal["INFO", "WARNING", "ERROR", "CRITICAL"],
        formato_log: str,
        nome_pacote: str
    ):
        super().__init__()
        self._configuracao_conexao = configuracao_conexao

        self.loger = logging.getLogger(nome_pacote)
        self.__FORMATO_LOG = formato_log
        self.__formater = logging.Formatter(self.__FORMATO_LOG)
        self.setFormatter(self.__formater)
        self.loger.setLevel(debug)

        # Evita a duplicação de logs se LogBanco instanciado mais de uma vez
        if not any(isinstance(h, LogBanco) for h in self.loger.handlers):
            self.loger.addHandler(self)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.__formater)
            console_handler.setLevel(logging.INFO)
            self.loger.addHandler(console_handler)

    @property
    def logger(self) -> logging.Logger:
        return self.loger

    @abstractmethod
    def emit(self, record: logging.LogRecord) -> None:
        pass
