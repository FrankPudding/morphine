import pytest

from morphine.domain.providers.factory import Factory
from tests.unit.conftest import DummyRepository, DummyService


class TestFactory:

    @pytest.fixture()
    def sut(self) -> Factory[DummyService]:
        return Factory(DummyService, "str", 1)

    def test_builds_correct_type(self, sut: Factory[DummyService]):
        # act
        dummy_service = sut()

        # assert
        assert isinstance(dummy_service, DummyService)

    def test_builds_new_instances(self, sut: Factory[DummyService]):
        # act
        dummy_service_1 = sut()
        dummy_service_2 = sut()

        # assert
        assert dummy_service_1 == dummy_service_1
        assert dummy_service_1 != dummy_service_2

    def test_override_dependencies(self, sut: Factory[DummyService]):
        # arrange
        new_args = tuple(["new_str"])
        new_kwargs = {"config_int": -1}

        # act
        sut.override_dependencies(*new_args, **new_kwargs)
        dummy_service = sut()

        # assert
        assert dummy_service.config_str == "new_str"
        assert dummy_service.config_int == -1

    def test_accepts_providers_in_constructor(self, sut: Factory[DummyService]):
        # arrange
        repository_factory = Factory(DummyRepository)

        # act
        sut.override_dependencies(config_int=-1, config_str="new_str", repository=repository_factory)

        # assert
        assert isinstance(sut().repository, DummyRepository)

