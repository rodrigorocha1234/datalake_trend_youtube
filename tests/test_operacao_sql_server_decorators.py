import pytest
from unittest.mock import MagicMock, patch

from src.operacao_banco.operacao.operacao_sql_server import OperacaoSqlServerLOG

# 1. Utilização de Decoradores com Pytest: @pytest.fixture
@pytest.fixture
def mock_contexto_banco():
    """
    Fixture (decorador implicitamente chamado) que prepara o cenário inicial (setup)
    para fornecer todas as dependências mockadas de banco de dados aos testes.
    A vantagem de decoradores de fixture é não poluir o corpo dos seus testes
    com configurações de mock repetitivas.
    """
    mock_conexao = MagicMock()
    mock_conexao.obter_parametros_conexao.return_value = (("connection_string_test",), {})
    
    mock_driver = MagicMock()
    mock_con = MagicMock()
    mock_cursor = MagicMock()
    
    # Amarrando os retornos
    mock_conexao.obter_driver.return_value = mock_driver
    mock_driver.return_value = mock_con
    mock_con.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Retornamos as instâncias de mock em um dicionário para usarmos asserts sobre elas depois
    return {
        "conexao": mock_conexao,
        "driver": mock_driver,
        "con": mock_con,
        "cursor": mock_cursor,
        "operacao": OperacaoSqlServerLOG(conexao=mock_conexao)
    }

# 2. Utilização de Decoradores Pytest Data-Driven: @pytest.mark.parametrize
@pytest.mark.parametrize("query_sql, query_param", [
    ("INSERT INTO logs (nivel) VALUES (?)", ("INFO",)),
    ("UPDATE logs SET nivel = ? WHERE id = ?", ("DEBUG", 2)),
    ("DELETE FROM logs WHERE nivel = ?", ("WARNING",))
])
def test_salvar_consulta_sucesso_parametrizada(mock_contexto_banco, query_sql, query_param):
    """
    Este teste possui dois "superpoderes" injetados via decoradores:
    
    O `@pytest.mark.parametrize` executa a função de teste de forma repetitiva para VÁRIOS valores diferentes (Data-Driven).
    Nesse contexto, ele testa um fluxo de salvamento de inserção, alteração e deleção com apenas 1 bloco de código.
    
    A instrução `mock_contexto_banco` injeta nossa @pytest.fixture configurada limpa acima a cada rodada.
    """
    # Resgatando o contexto limpo para este teste
    operacao = mock_contexto_banco["operacao"]
    mock_driver = mock_contexto_banco["driver"]
    mock_con = mock_contexto_banco["con"]
    mock_cursor = mock_contexto_banco["cursor"]

    # Ação acionando o método oficial de envio
    operacao.salvar_consulta(query_sql, query_param)

    # Asserções validando as ordens e chamadas exatas que o mock recebeu
    mock_driver.assert_called_once_with("connection_string_test")
    mock_cursor.execute.assert_called_once_with(query_sql, query_param)
    mock_con.commit.assert_called_once()
    mock_con.close.assert_called_once()

# 3. Utilização de Decoradores da lib nativa Unittest: @patch
@patch("builtins.print")
def test_salvar_consulta_com_patch_decorator(mock_print, mock_contexto_banco):
    """
    O decorador `@patch` injeta o objeto mockeado diretamente na declaração da função (o `mock_print`).
    Ele sobrecreve temporariamente a função 'print()' nativa do Python (builtins.print), nos dando 
    acesso às verificações que ocorreram dentro do bloco nativo `except Exception as e:` que o seu script tem.
    """
    operacao = mock_contexto_banco["operacao"]
    mock_con = mock_contexto_banco["con"]
    mock_cursor = mock_contexto_banco["cursor"]

    # Causando uma falha grave na inserção
    erro_estimulado = Exception("Timeout de banco de dados simulado")
    mock_cursor.execute.side_effect = erro_estimulado

    # Ação - O código continuará funcionando e passará pelo `except`
    operacao.salvar_consulta("SELECT 'Erro de execucao!'", ())

    # Asserções focadas na falha
    
    # Averigua se fomos capazes de printar via mock @patch interceptor
    mock_print.assert_called_once_with(erro_estimulado)
    
    # Averigua as lógicas essenciais
    mock_con.commit.assert_not_called()  # Bloqueado pelo erro
    mock_con.close.assert_called_once()  # Sempre fechado devido a robustez do 'finally'
