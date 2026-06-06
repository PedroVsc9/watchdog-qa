import pytest

from src.helpers import (
    assert_content_type_json,
    assert_field_type,
    assert_pagination,
    assert_response_time,
    assert_status_code,
)


@pytest.mark.contract
def test_contract_content_type(client):
    response = client.get("/posts")
    assert_status_code(response, 200)
    assert_content_type_json(response)


@pytest.mark.contract
def test_contract_response_time(client):
    response = client.get("/posts")
    assert_status_code(response, 200)
    assert_response_time(response, max_ms=2000)


@pytest.mark.contract
def test_contract_field_types(client):
    response = client.get("/posts/1")
    assert_status_code(response, 200)
    payload = response.json()
    assert_field_type(payload, "id", int)
    assert_field_type(payload, "title", str)
    assert_field_type(payload, "active", bool)


@pytest.mark.contract
def test_contract_pagination(client):
    response = client.get("/posts", params={"page": 1, "limit": 10})
    assert_status_code(response, 200)
    payload = response.json()
    assert_pagination(payload)
