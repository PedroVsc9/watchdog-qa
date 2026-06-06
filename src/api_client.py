import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, Optional


class APIClient:
    def __init__(self, config: Dict[str, Any]):
        self.base_url = config["base_url"].rstrip("/")
        self.timeout = config.get("timeout", 30)
        self.auth_config = config.get("auth", {})
        self.session = requests.Session()
        self._apply_authentication()

    def _apply_authentication(self) -> None:
        auth_type = self.auth_config.get("type", "none").lower()

        if auth_type == "bearer":
            token = self.auth_config.get("bearer_token", "")
            if token:
                self.session.headers.update({"Authorization": f"Bearer {token}"})

        elif auth_type == "basic":
            username = self.auth_config.get("username", "")
            password = self.auth_config.get("password", "")
            if username or password:
                self.session.auth = HTTPBasicAuth(username, password)

        elif auth_type == "api_key":
            api_key = self.auth_config.get("api_key", "")
            api_key_name = self.auth_config.get("api_key_name", "X-API-KEY")
            if api_key:
                self.session.headers.update({api_key_name: api_key})

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        url = path if path.startswith("http") else f"{self.base_url}/{path.lstrip('/') }"
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            timeout=self.timeout,
        )
        return response

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path: str, json: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self._request("POST", path, json=json, headers=headers)

    def put(self, path: str, json: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self._request("PUT", path, json=json, headers=headers)

    def patch(self, path: str, json: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self._request("PATCH", path, json=json, headers=headers)

    def delete(self, path: str, json: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self._request("DELETE", path, json=json, headers=headers)
