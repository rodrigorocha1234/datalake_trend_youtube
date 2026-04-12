from typing import Any, Tuple

from minio import Minio

from src.operacao_banco.config.idb_config import IDbConfig
from src.operacao_banco.config.protocols import MinioConnect


class OperacaoMInioS3:
    def __init__(self, conexao_s3: IDbConfig[Minio, MinioConnect]):
        self.__conexao_s3 = conexao_s3

    def salvar_dados(self, dado: Tuple[str, Tuple[Any, ...]], **kwargs: Any) -> None:
        self.__conexao_s3.obter_driver()

        pass
