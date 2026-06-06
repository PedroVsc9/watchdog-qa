import pytest
from src.helpers import assert_status_code, assert_content_type_json


@pytest.mark.functional
def test_get_resource_list(client):
    # TODO: Atualize o path abaixo para um endpoint válido do seu serviço
    response = client.get("/resources")
    assert_status_code(response, 200)
    assert_content_type_json(response)


@pytest.mark.functional
def test_create_resource(client):
    # TODO: Ajuste o payload conforme o contrato da sua API
    payload = {"name": "exemplo", "active": True}
    response = client.post("/resources", json=payload)
    assert_status_code(response, 201)
    assert_content_type_json(response)


@pytest.mark.functional
def test_delete_resource(client):
    # TODO: Substitua pelo ID de um recurso que possa ser removido ou mockado
    response = client.delete("/resources/1")
    assert response.status_code in (200, 204)


@pytest.mark.functional
def test_list_pagination(client):
    response = client.get("/resources", params={"page": 1, "limit": 10})
    assert_status_code(response, 200)
    assert_content_type_json(response)
