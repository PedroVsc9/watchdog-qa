# api-test-template

[![CI](https://github.com/PedroVsc9/api-test-template/actions/workflows/tests.yml/badge.svg)](https://github.com/PedroVsc9/api-test-template/actions/workflows/tests.yml)

Template genérico de automação de testes de API em Python. Qualquer QA pode clonar este projeto, ajustar `config/settings.ini` e começar a escrever testes imediatamente.

## Como usar em um novo projeto

1. Clone o repositório.
2. Atualize `config/settings.ini` com a URL da API e as credenciais corretas.
3. Instale dependências: `pip install -r requirements.txt`.
4. Execute `pytest` para rodar os testes.

## Tipos de teste

| Tipo | O que cobre | Onde escrever |
|---|---|---|
| functional | Verifica comportamento e fluxo da API | `tests/functional/` |
| contract | Valida contrato de resposta e qualidade de payload | `tests/contract/` |
| regression | Cobertura de edge cases e comportamentos inválidos | `tests/regression/` |

## Exemplo de uso

```python
from src.config_loader import ConfigLoader
from src.api_client import APIClient

config = ConfigLoader().load()
client = APIClient(config)

response = client.get('/users')
assert response.status_code == 200
```

## Exemplos de código de teste

```python
import pytest
from src.config_loader import ConfigLoader
from src.api_client import APIClient

@pytest.fixture(scope='session')
def client():
    config = ConfigLoader().load()
    return APIClient(config)

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
```

> Altere apenas `config/settings.ini` para usar o template em outro projeto.
