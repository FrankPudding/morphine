import pytest

from morphine.domain.providers.singleton import Singleton
from tests.unit.conftest import DummyService


class TestSingleton:
    @pytest.fixture()
    def sut(self) -> Singleton[DummyService]:
        return Singleton(DummyService, "str", 1)

    def test_call(self, sut: Singleton[DummyService]):
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
