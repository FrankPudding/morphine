from typing import Protocol

import pytest

from morphine import Container
from morphine.domain.dependencies.factory import Factory


class JunkRepository(Protocol):
    pass


class JunkRepository1:
    pass


class JunkRepository2:
    pass


class JunkService:
    def __init__(self, repository):
        self.repository = repository


class JunkContainer(Container):
    junk_repository1 = Factory(JunkRepository1)
    junk_repository2 = Factory(JunkRepository2)
    junk_repository: Factory[JunkRepository] = junk_repository1
    junk_service = Factory(JunkService, repository=junk_repository)


class TestContainer:
    @pytest.fixture()
    def sut(self) -> JunkContainer:
        return JunkContainer()

    def test_overrides(self, sut: JunkContainer):
        # act
        assert isinstance(sut.junk_service().repository, JunkRepository1)
        assert sut.junk_service() != sut.junk_repository2
        sut.junk_repository.override(sut.junk_repository2)

        # assert
        assert isinstance(sut.junk_service().repository, JunkRepository2)
