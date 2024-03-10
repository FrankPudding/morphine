from typing import Protocol

import pytest

from morphine import Container
from morphine.domain.providers.factory import Factory


class DummyRepository(Protocol):
    pass


class DummyRepository1:
    pass


class DummyRepository2:
    pass


class DummyService:
    def __init__(self, repository):
        self.repository = repository


class DummyContainer(Container):
    dummy_repository1 = Factory(DummyRepository1)
    dummy_repository2 = Factory(DummyRepository2)
    dummy_repository: Factory[DummyRepository] = dummy_repository1
    dummy_service = Factory(DummyService, repository=dummy_repository)


class TestContainer:
    @pytest.fixture()
    def sut(self) -> DummyContainer:
        return DummyContainer()

    def test_overrides(self, sut: DummyContainer):
        # act
        assert isinstance(sut.dummy_service().repository, DummyRepository1)
        assert sut.dummy_service() != sut.dummy_repository2
        sut.dummy_repository.override(sut.dummy_repository2)

        # assert
        assert isinstance(sut.dummy_service().repository, DummyRepository2)
