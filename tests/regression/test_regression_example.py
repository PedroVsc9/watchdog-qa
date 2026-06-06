import pytest
from src.helpers import assert_status_code


@pytest.mark.regression
def test_regression_id_zero(client):
    # ID zero é um caso comum de edge case em APIs que esperam IDs positivos.
    response = client.get("/posts/0")
    assert response.status_code in (400, 404)


@pytest.mark.regression
def test_regression_negative_id(client):
    # IDs negativos devem ser rejeitados ou tratados explicitamente.
    response = client.get("/posts/-1")
    assert response.status_code in (400, 404)


@pytest.mark.regression
def test_regression_invalid_id(client):
    # IDs inválidos ajudam a validar sanitização de parâmetros.
    response = client.get("/posts/abc")
    assert response.status_code in (400, 404)


@pytest.mark.regression
def test_regression_post_without_body(client):
    # Verifica comportamento ao criar recurso sem payload.
    response = client.post("/posts", json=None)
    assert response.status_code == 201


@pytest.mark.regression
def test_regression_limit_too_high(client):
    # Testa limite elevado de itens para garantir retorno controlado.
    response = client.get("/posts", params={"page": 1, "limit": 10000})
    assert_status_code(response, 200)
    assert isinstance(response.json(), list)
