from src.servicos.banco.interfaces.ioperacao import IOperacao


class OperacaoMInioS3(IOperacao):
    def __init__(self, conexao_s3: IOperacao):
        self.__conexao_s3 = conexao_s3

    def checar_conexao(self) -> bool:
        return True

    def salvar_dados(self, **kwargs) -> None:
        pass
