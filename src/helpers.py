from typing import Any, Dict, List


def assert_status_code(response, expected_status: int) -> None:
    assert response.status_code == expected_status, f"Esperado {expected_status}, obteve {response.status_code}"


def assert_response_time(response, max_ms: int) -> None:
    assert response.elapsed.total_seconds() * 1000 <= max_ms, (
        f"Tempo de resposta maior que {max_ms}ms: {response.elapsed.total_seconds() * 1000:.2f}ms"
    )


def assert_has_keys(payload: Dict[str, Any], expected_keys: List[str]) -> None:
    missing = [key for key in expected_keys if key not in payload]
    assert not missing, f"Chaves ausentes na resposta: {missing}"


def assert_list_not_empty(items: List[Any]) -> None:
    assert isinstance(items, list), "Payload não é uma lista"
    assert items, "Lista de resposta está vazia"


def assert_content_type_json(response) -> None:
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, f"Content-Type inesperado: {content_type}"


def assert_field_type(payload: Dict[str, Any], field_name: str, expected_type: type) -> None:
    assert field_name in payload, f"Campo {field_name} não encontrado"
    assert isinstance(payload[field_name], expected_type), (
        f"Campo {field_name} deve ser {expected_type.__name__} mas foi {type(payload[field_name]).__name__}"
    )


def assert_pagination(payload: Dict[str, Any]) -> None:
    assert_has_keys(payload, ["page", "limit", "total", "items"])
    assert isinstance(payload["items"], list), "Campo items deve ser uma lista"
