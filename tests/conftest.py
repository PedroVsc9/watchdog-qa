import pytest

from src.config_loader import ConfigLoader
from src.api_client import APIClient


@pytest.fixture(scope="session")
def client():
    """Cliente HTTP compartilhado para todos os testes de API."""
    config = ConfigLoader().load()
    return APIClient(config)


# Adicione fixtures de projetos específicos aqui.
# Por exemplo: login_token, test_data, ambiente de dados, clientes especializados, etc.
