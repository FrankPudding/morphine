import pytest

from morphine.domain.dependencies.factory import Factory


class JunkService:
    def __init__(self, config_str: str, config_int: int):
        self.config_str = config_str
        self.config_int = config_int


class TestFactory:

    @pytest.fixture()
    def sut(self) -> Factory[JunkService]:
        return Factory(JunkService, "str", 1)

    def test_builds_correct_type(self, sut: Factory[JunkService]):
        # act
        junk_service = sut()

        # assert
        assert isinstance(junk_service, JunkService)

    def test_builds_new_instances(self, sut: Factory[JunkService]):
        # act
        junk_service_1 = sut()
        junk_service_2 = sut()

        # assert
        assert junk_service_1 == junk_service_1
        assert junk_service_1 != junk_service_2

    def test_override_dependencies(self, sut: Factory[JunkService]):
        # arrange
        new_args = tuple(["new_str"])
        new_kwargs = {"config_int": -1}

        # act
        sut.override_dependencies(*new_args, **new_kwargs)
        junk_service = sut()

        # assert
        assert junk_service.config_str == "new_str"
        assert junk_service.config_int == -1
