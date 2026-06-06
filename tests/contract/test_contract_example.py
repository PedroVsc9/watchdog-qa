from src.helpers import (
    assert_content_type_json,
    assert_field_type,
    assert_pagination,
    assert_response_time,
    assert_status_code,
)


def test_contract_content_type(client):
    response = client.get("/resources")
    assert_status_code(response, 200)
    assert_content_type_json(response)


def test_contract_response_time(client):
    response = client.get("/resources")
    assert_status_code(response, 200)
    assert_response_time(response, max_ms=2000)


def test_contract_field_types(client):
    response = client.get("/resources/1")
    assert_status_code(response, 200)
    payload = response.json()
    assert_field_type(payload, "id", int)
    assert_field_type(payload, "name", str)
    assert_field_type(payload, "active", bool)


def test_contract_pagination(client):
    response = client.get("/resources", params={"page": 1, "limit": 10})
    assert_status_code(response, 200)
    payload = response.json()
    assert_pagination(payload)
