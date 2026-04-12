from unittest.mock import MagicMock
import pytest

from src.operacao_banco.operacao.operacao_sql_server import OperacaoSqlServerLOG


def test_salvar_consulta_sucesso():
    """
    Testa o fluxo de salvar uma consulta no banco de dados com sucesso.
    
    Este teste verifica:
    1. Se o driver e as strings de conexão foram extraídos da classe de config passada injeção.
    2. Se a conexão (driver) foi instanciada com os parâmetros corretos.
    3. Se o cursor foi criado, e 'execute' convocado estritamente com os argumentos fornecidos.
    4. Se o método commit() foi acionado para efetivar a gravação no banco.
    5. Se a conexão foi devidamente encerrada (close()), liberando a porta/conexão.
    """
    # 1. Configurando o objeto de conexão mock que simula o IDbConfig
    mock_conexao = MagicMock()
    mock_conexao.obter_parametros_conexao.return_value = (("string_conexao=log",), {"timeout": 30})
    
    mock_driver = MagicMock()
    mock_con = MagicMock()
    mock_cursor = MagicMock()
    
    # Quando obter_driver for chamado, ele retonará nosso mock_driver
    mock_conexao.obter_driver.return_value = mock_driver
    # Quando o driver for chamado com os parâmetros, criará nossa mock_con
    mock_driver.return_value = mock_con
    
    # O mock_con.cursor() atua como um gerenciador de contexto (`with con.cursor() as cursor:`)
    # Por isso configuramos o '__enter__' para retornar o nosso mock_cursor
    mock_con.cursor.return_value.__enter__.return_value = mock_cursor

    operacao = OperacaoSqlServerLOG(conexao=mock_conexao)
    
    sql = "INSERT INTO logs (nivel) VALUES (?)"
    param = ("INFO",)
    
    # 2. Ação: Chamando o método para gravar no banco
    operacao.salvar_consulta(sql, param)
    
    # 3. Asserções (Verificando comportamentos)
    mock_driver.assert_called_once_with("string_conexao=log", timeout=30)
    mock_con.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(sql, param)
    mock_con.commit.assert_called_once()
    mock_con.close.assert_called_once()


def test_salvar_consulta_com_excecao(capsys):
    """
    Testa o comportamento do script ao encontrar um erro vindo de falha de query.
    
    Este teste verifica o controle de fluxo (try-except-finally):
    1. Simula um erro de Exception ocorrendo bem em `cursor.execute()`.
    2. Verifica que a execução falha e cai no bloco `except`, printando o erro (checado capturando o sys.stdout usando o 'capsys' do pytest).
    3. Verifica que o commit não é chamado porque falhou na query executada antes.
    4. Verifica que o método .close() é executado obrigatoriamente dentro do `finally` para não persistir em estado vulnerável.
    """
    mock_conexao = MagicMock()
    mock_conexao.obter_parametros_conexao.return_value = ((), {})
    
    mock_driver = MagicMock()
    mock_con = MagicMock()
    mock_cursor = MagicMock()
    
    mock_driver.return_value = mock_con
    mock_conexao.obter_driver.return_value = mock_driver
    
    mock_con.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Aqui ensinamos o Mock a causar um erro na hora do comando execute do SQL Server
    mock_cursor.execute.side_effect = Exception("Erro simulado do banco SQL Server")

    operacao = OperacaoSqlServerLOG(conexao=mock_conexao)
    
    sql = "INSERT INTO logs (nivel) VALUES (?)"
    param = ("INFO",)
    
    # Ação
    operacao.salvar_consulta(sql, param)
    
    # Captura dos prints emitidos no console para testar o tratador
    print_saidas = capsys.readouterr()
    
    # Asserções
    assert "Erro simulado do banco SQL Server" in print_saidas.out
    mock_con.commit.assert_not_called()  # Não pode comitar dados incorretos ou não transacionados integralmente!
    mock_con.close.assert_called_once()  # Sempre fechando conexões para evitar memory leak
