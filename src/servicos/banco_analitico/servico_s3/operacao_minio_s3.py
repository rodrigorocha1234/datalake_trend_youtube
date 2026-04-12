from typing import Any, Tuple

from minio import Minio

from src.servicos.operacao_banco.config.idb_config import IDbConfig
from src.servicos.operacao_banco.config.protocols import MinioConnect
from src.servicos.operacao_banco.operacao.ioperacao import IOperacao


class OperacaoMInioS3(IOperacao):
    def __init__(self, conexao_s3: IDbConfig[Minio, MinioConnect]):
        self.__conexao_s3 = conexao_s3

    def checar_conexao(self) -> bool:
        return True

    def salvar_dados(self, sql: str, param: Tuple[Any, ...]) -> None:
        pass
