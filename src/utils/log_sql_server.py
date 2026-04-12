
import logging
from datetime import datetime
from typing import Literal

from src.servicos.operacao_banco.config.idb_config import IDbConfig
from src.servicos.operacao_banco.operacao.operacao_sql_server import \
    OperacaoSqlServer
from src.utils.log_banco import LogBanco


class LogBancoSQLServer(LogBanco):
    def __init__(
        self,
        configuracao_conexao: IDbConfig,
        debug: Literal["INFO", "WARNING", "ERROR", "CRITICAL"],
        formato_log: str,
        nome_pacote: str
    ):
        super().__init__(
            debug=debug,
            formato_log=formato_log,
            nome_pacote=nome_pacote,
            configuracao_conexao=configuracao_conexao
        )
        self.__operacao = OperacaoSqlServer(conexao=configuracao_conexao)

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

        self.__operacao.salvar_dados(dado=(sql, params))
