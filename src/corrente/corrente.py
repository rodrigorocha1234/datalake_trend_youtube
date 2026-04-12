from src.contexto.contexto import Contexto
from typing import Optional
from abc import ABC, abstractmethod

from src.utils.log_banco import LogBanco


class Corrente(ABC):
    def __init__(self, conexao_log: LogBanco):
        self._conexao_log = conexao_log
        self._proxima_corrente: Optional["Corrente"] = None

    def criar_proxima_corrente(self, corrente: "Corrente"):
        self._proxima_corrente = corrente
        return corrente

    def corrente(self, contexto: Contexto):
        self._conexao_log.loger.info("Iniciando Pipeline")
        if self.executar_processo(contexto):
            self._conexao_log.loger.info(
                f'{self.__class__.__name__} -> Sucesso ao executar')
            if self._proxima_corrente:
                self._proxima_corrente.corrente(contexto)
            else:
                self._conexao_log.loger.info(
                    f'{self.__class__.__name__} ->  Última corrente da cadeia')
        else:
            self._conexao_log.loger.error(
                f"ERRO ao executar pipeline {self.__class__.__name__}")

    @abstractmethod
    def executar_processo(self, contexto: Contexto) -> bool:
        return True
