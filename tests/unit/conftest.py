from typing import Optional


class DummyRepository:
    pass


class DummyService:
    def __init__(self, config_str: str, config_int: int, repository: Optional[DummyRepository] = None):
        self.config_str = config_str
        self.config_int = config_int
        self.repository = repository
