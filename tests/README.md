# 🧪 Testes Unitários - Cotação USD-BRL

Esta pasta contém os testes unitários para o endpoint de cotação USD-BRL.

## 📁 Arquivos

- `test_exchange.py` - Testes usando **unittest** (biblioteca padrão do Python)
- `test_exchange_pytest.py` - Testes usando **pytest** (mais moderno)

## ✅ Como Executar os Testes

### Opção 1: Usando pytest (Recomendado)

```bash
# Executar todos os testes
pytest tests/

# Executar com mais detalhes
pytest tests/ -v

# Executar apenas um arquivo
pytest tests/test_exchange_pytest.py -v

# Executar com cobertura
pytest tests/ --cov=app --cov-report=term-missing
```

### Opção 2: Usando unittest

```bash
# Executar os testes
python -m unittest tests/test_exchange.py

# Executar com mais detalhes
python -m unittest tests/test_exchange.py -v
```

## 🎯 O que os Testes Cobrem

### Testes de Serviço (`get_usd_brl_rate`)
- ✅ Obtenção de cotação com sucesso (mock)
- ✅ Erro na API externa (mock)
- ✅ Dados ausentes na resposta (mock)
- ✅ Timeout na conexão (mock)

### Testes de Endpoint (`/api/exchange/usd-to-brl`)
- ✅ Requisição bem-sucedida (mock)
- ✅ Erro na API externa (mock)

## 🔧 Importante: Uso de Mocks

**Todos os testes usam `unittest.mock.patch` para simular as chamadas à API externa.**

Isso significa que:
- ❌ **NENHUMA chamada real é feita** para https://economia.awesomeapi.com.br
- ✅ Os testes são **rápidos** (não dependem de rede)
- ✅ Os testes são **independentes** (não dependem da API estar online)
- ✅ Os testes são **previsíveis** (sempre retornam o mesmo resultado)

### Exemplo de Mock:

```python
@patch('app.service.requests.get')
def test_get_usd_brl_rate_success(self, mock_get):
    # Simula a resposta da API
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"USDBRL": {...}}
    mock_get.return_value = mock_response
    
    # Agora quando get_usd_brl_rate() chamar requests.get(),
    # ele receberá a resposta mockada, não fará chamada real
```

## 📊 Exemplo de Saída

```bash
$ pytest tests/test_exchange_pytest.py -v

tests/test_exchange_pytest.py::TestExchangeService::test_get_usd_brl_rate_success PASSED
tests/test_exchange_pytest.py::TestExchangeService::test_get_usd_brl_rate_api_error PASSED
tests/test_exchange_pytest.py::TestExchangeService::test_get_usd_brl_rate_missing_data PASSED
tests/test_exchange_pytest.py::TestExchangeEndpoint::test_endpoint_success PASSED
tests/test_exchange_pytest.py::TestExchangeEndpoint::test_endpoint_api_error PASSED

========================== 5 passed in 0.12s ==========================
```

## 🎓 Requisitos Atendidos

✅ Testes unitários na pasta `/tests`  
✅ Uso de `unittest.mock.patch` para mockar API externa  
✅ Nenhuma chamada real à AwesomeAPI  
✅ Testes rápidos e independentes  
✅ Cobertura da lógica de serviço  
✅ Cobertura do endpoint  

## 📝 Notas

- Os testes verificam tanto casos de **sucesso** quanto de **erro**
- Todos os mocks simulam respostas reais da AwesomeAPI
- Os testes garantem que a integração funciona sem depender da API externa

