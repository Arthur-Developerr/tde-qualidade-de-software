"""
Testes unitários para o endpoint de cotação USD-BRL (usando pytest)
"""
import pytest
from unittest.mock import patch, MagicMock
from app.app import app
from app.service import get_usd_brl_rate


@pytest.fixture
def client():
    """Fixture para criar cliente de teste do Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestExchangeService:
    """Testes para o serviço de cotação USD-BRL"""
    
    @patch('app.service.requests.get')
    def test_get_usd_brl_rate_success(self, mock_get):
        """Testa obtenção de cotação com sucesso usando mock"""
        # Mock da resposta da API externa
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "USDBRL": {
                "code": "USD",
                "codein": "BRL",
                "name": "Dólar Americano/Real Brasileiro",
                "high": "5.4251",
                "low": "5.37139",
                "varBid": "-0.0035",
                "pctChange": "-0.064791",
                "bid": "5.3986",
                "ask": "5.4016",
                "timestamp": "1763990550",
                "create_date": "2025-11-24 10:22:30"
            }
        }
        mock_get.return_value = mock_response
        
        # Executa a função
        result, status_code = get_usd_brl_rate()
        
        # Verificações
        assert status_code == 200
        assert result["code"] == "USD"
        assert result["codein"] == "BRL"
        assert result["bid"] == "5.3986"
        assert result["ask"] == "5.4016"
        assert result["name"] == "Dólar Americano/Real Brasileiro"
        
        # Verifica que a URL correta foi chamada
        mock_get.assert_called_once_with(
            "https://economia.awesomeapi.com.br/json/last/USD-BRL",
            timeout=10
        )
    
    @patch('app.service.requests.get')
    def test_get_usd_brl_rate_api_error(self, mock_get):
        """Testa quando a API externa retorna erro"""
        # Mock de erro na API
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        # Executa a função
        result, status_code = get_usd_brl_rate()
        
        # Verificações
        assert status_code == 500
        assert "error" in result
    
    @patch('app.service.requests.get')
    def test_get_usd_brl_rate_missing_data(self, mock_get):
        """Testa quando a API não retorna os dados esperados"""
        # Mock de resposta sem dados
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}  # Sem o campo USDBRL
        mock_get.return_value = mock_response
        
        # Executa a função
        result, status_code = get_usd_brl_rate()
        
        # Verificações
        assert status_code == 404
        assert "error" in result


class TestExchangeEndpoint:
    """Testes para o endpoint /api/exchange/usd-to-brl"""
    
    @patch('app.service.requests.get')
    def test_endpoint_success(self, mock_get, client):
        """Testa endpoint retornando dados com sucesso"""
        # Mock da resposta da API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "USDBRL": {
                "code": "USD",
                "codein": "BRL",
                "name": "Dólar Americano/Real Brasileiro",
                "high": "5.4251",
                "low": "5.37139",
                "varBid": "-0.0035",
                "pctChange": "-0.064791",
                "bid": "5.3986",
                "ask": "5.4016",
                "timestamp": "1763990550",
                "create_date": "2025-11-24 10:22:30"
            }
        }
        mock_get.return_value = mock_response
        
        # Faz requisição
        response = client.get('/api/exchange/usd-to-brl')
        
        # Verificações
        assert response.status_code == 200
        data = response.get_json()
        assert data["code"] == "USD"
        assert data["codein"] == "BRL"
        assert "bid" in data
        assert "ask" in data
        assert "high" in data
        assert "low" in data
    
    @patch('app.service.requests.get')
    def test_endpoint_api_error(self, mock_get, client):
        """Testa endpoint quando API externa falha"""
        # Mock de erro
        mock_response = MagicMock()
        mock_response.status_code = 503
        mock_get.return_value = mock_response
        
        # Faz requisição
        response = client.get('/api/exchange/usd-to-brl')
        
        # Verificações
        assert response.status_code == 503
        data = response.get_json()
        assert "error" in data

