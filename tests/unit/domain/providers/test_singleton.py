import pytest

from morphine.providers.singleton import Singleton
from tests.unit.conftest import DummyRepository, DummyService


class TestSingleton:
    @pytest.fixture()
    def sut(self) -> Singleton[DummyService]:
        return Singleton(DummyService, "str", 1)

    def test_builds_correct_type(self, sut: Singleton[DummyService]):
        # act
        dummy_service = sut()

        # assert
        assert isinstance(dummy_service, DummyService)

    def test_returns_same_instance(self, sut: Singleton[DummyService]):
        # act
        dummy_service_1 = sut()
        dummy_service_2 = sut()

        # assert
        assert dummy_service_1 == dummy_service_2

    def test_reset(self, sut: Singleton[DummyService]):
        # arrange
        dummy_service_1 = sut()

        # act
        sut.reset()
        dummy_service_2 = sut()

        # arrange
        assert dummy_service_1 != dummy_service_2

    def test_accepts_providers_in_constructor(
        self, sut: Singleton[DummyService]
    ):
        # arrange
        repository_factory = Singleton(DummyRepository)

        # act
        sut.override_dependencies(
            config_int=-1, config_str="new_str", repository=repository_factory
        )

        # assert
        assert isinstance(sut().repository, DummyRepository)
