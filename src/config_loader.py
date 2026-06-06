import os
from configparser import ConfigParser


def _to_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class ConfigLoader:
    def __init__(self, path: str = "config/settings.ini"):
        self.path = path
        self.parser = ConfigParser()

    def load(self) -> dict:
        self.parser.read(self.path)

        api_config = self.parser["api"] if "api" in self.parser else {}
        auth_config = self.parser["auth"] if "auth" in self.parser else {}
        endpoints = self.parser["endpoints"] if "endpoints" in self.parser else {}

        config = {
            "base_url": os.getenv("API_BASE_URL", api_config.get("base_url", "")).rstrip("/"),
            "timeout": _to_int(os.getenv("API_TIMEOUT", api_config.get("timeout", "30")), 30),
            "auth": {
                "type": auth_config.get("type", "none").lower(),
                "bearer_token": auth_config.get("bearer_token", ""),
                "username": auth_config.get("username", ""),
                "password": auth_config.get("password", ""),
                "api_key": auth_config.get("api_key", ""),
                "api_key_name": auth_config.get("api_key_name", "X-API-KEY"),
            },
            "endpoints": dict(endpoints),
        }

        if not config["base_url"]:
            raise ValueError("API base_url não foi informada em config/settings.ini ou em API_BASE_URL")

        return config
