import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime

from src.servicos.api_youtube.api_youtube import YoutubeAPI
from src.utils.log_banco import LogBanco

# Injetando uma classe estática (Config) para não poluir ou forçar chaves de API reais
@pytest.fixture(autouse=True)
def mock_config(monkeypatch):
    """
    Substitui as constantes da sua de Config para rodar o os testes 
    mesmo sem uma variável de ambiente real CHAVE_API_YOUTUBE.
    """
    monkeypatch.setattr("src.servicos.api_youtube.api_youtube.Config.CHAVE_API_YOUTUBE", "API_YOUTUBE_TESTE")

@pytest.fixture
def mock_dependencias_api():
    """
    Fornece as dependências puras mockadas para testes, como o banco de logs,
    sem invocar construções desnecessárias.
    """
    mock_log = MagicMock()
    mock_log.loger = MagicMock()
    return {
        "log": mock_log
    }

def test_checar_conexao_sucesso(mock_dependencias_api):
    """
    Testa se o método `checar_conexao` flui corretamente na situação padrão (sucesso 200).
    Usando contexto @patch nativo via "with" ou decorador para o googleapiclient.build.
    """
    log = mock_dependencias_api["log"]
    
    # Faz o mock do serviço Youtube construído pelo 'build()' retornado para o sistema 
    with patch("src.servicos.api_youtube.api_youtube.build") as mock_build:
        
        # Simulando uma resposta da request list().execute()
        # build().videos().list().execute() chaining
        mock_youtube_resource = MagicMock()
        mock_build.return_value = mock_youtube_resource
        
        # Declarando a instância controlada a ser testada
        api = YoutubeAPI(conexao_log=log)
        
        resultado = api.checar_conexao()
        
        # Validando o fluxo
        assert resultado is True
        mock_youtube_resource.videos().list().execute.assert_called_once()
        log.loger.error.assert_not_called()

@patch("src.servicos.api_youtube.api_youtube.build")
def test_checar_conexao_falha(mock_build, mock_dependencias_api):
    """
    Testa a falha forçada com o decorador `@patch` capturando o "build" local.
    Verificamos se retornará `False` validamente e emitirá um Error pro Banco de Log de forma transparente.
    """
    log = mock_dependencias_api["log"]
    
    mock_youtube_resource = MagicMock()
    mock_build.return_value = mock_youtube_resource
    
    # Simulando um erro estourando de HTTP/API Youtube
    erro_teste = Exception("403 Forbidden Quota Exceeded")
    mock_youtube_resource.videos().list().execute.side_effect = erro_teste
    
    # Declarando e ativando a rotina
    api = YoutubeAPI(conexao_log=log)
    resultado = api.checar_conexao()
    
    # Asserções
    assert resultado is False
    log.loger.error.assert_called_once()
    
    # Conferindo se o erro injetado passou adequadamente pro registro do logger 
    args, kwargs = log.loger.error.call_args
    assert kwargs["extra"]["codigo"] == 500
    assert kwargs["extra"]["requisicao"] == erro_teste

@patch("src.servicos.api_youtube.api_youtube.build")
def test_obter_video_por_data_paginado(mock_build, mock_dependencias_api):
    """
    Testa o algoritmo de Gerador `yield` para certificar se ele compreende a leitura
    da flag "nextPageToken" varrendo continuamente enquanto possui páginas remanescentes no Google.
    """
    log = mock_dependencias_api["log"]
    
    mock_youtube_resource = MagicMock()
    mock_build.return_value = mock_youtube_resource
    
    # Preparando respostas paginadas sucessivas.
    # O mock_execute devolverá duas páginas consecutivas ao ser chamado em loop!
    pagina_1 = {
        "items": [{"id": "v1"}, {"id": "v2"}], 
        "nextPageToken": "TOKEN_CHAVE_2"
    }
    pagina_2 = {
        "items": [{"id": "v3"}] 
        # Sem nextPageToken induzindo ao erro "KeyError" para parada inteligente da sua class
    }
    
    # O side_effect recebendo lista emite cada item por vez cada vez que .execute() for chamado no while
    mock_youtube_resource.search().list().execute.side_effect = [pagina_1, pagina_2]
    
    api = YoutubeAPI(conexao_log=log)
    
    # Consumindo o Generator
    videos_resultantes = list(api.obter_video_por_data(datetime(2025, 1, 1)))
    
    # Asserções finais
    assert len(videos_resultantes) == 3
    assert videos_resultantes[0]["id"] == "v1"
    assert videos_resultantes[2]["id"] == "v3"
    
    # Esperamos que o search().list() tenha ocorrido duas vezes exatas e o log duas vezes
    assert mock_youtube_resource.search().list().execute.call_count == 2
    assert log.loger.info.call_count == 2
