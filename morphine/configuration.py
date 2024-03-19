from typing import Any, Dict


class Configuration:
    _config_dict: Dict[str, Any]

    def __getattr__(self, item: str):
        return self._config_dict.get(item)

    def from_dict(self, config: Dict[str, Any]):
        if not isinstance(config, Dict):
            raise TypeError("Must provide a dictionary to from_dict")
        self._config_dict = config
