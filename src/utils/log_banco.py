
import logging
from datetime import datetime
from typing import Literal

from src.operacao_banco.operacao.Ioperacao import IOperacao


class LogBanco(logging.Handler):

    def __init__(
        self,
        db_operacao: IOperacao,
        debug: Literal["INFO", "WARNING", "ERROR", "CRITICAL"],
        formato_log: str,
        nome_pacote: str
    ):
        super().__init__()
        self.__db_operacao = db_operacao

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

    def emit(self, record: logging.LogRecord) -> None:
        self.format(record)

        timestamp = datetime.fromtimestamp(record.created)

        status_code = getattr(record, 'status_code', None)
        mensagem_de_excecao_tecnica = getattr(
            record, 'mensagem_de_excecao_tecnica', None)
        requisicao = getattr(record, 'requisicao', None)
        url = getattr(record, 'url', None)

        sql = '''
        INSERT INTO logs (
            [timestamp],
            [level],
            [message],
            [logger_name],
            [filename],
            [func_name],
            [line_no],
            [url],
            [mensagem_de_excecao_tecnica],
            [requisicao],
            [status_code]
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        params = (
            timestamp,
            record.levelname,
            record.getMessage(),
            record.name,
            record.filename,
            record.funcName,
            record.lineno,
            url,
            mensagem_de_excecao_tecnica,
            requisicao,
            status_code
        )

        self.__db_operacao.salvar_dados(sql=sql, param=params)
