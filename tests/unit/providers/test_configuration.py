import pytest

from morphine.configuration import Configuration


class TestConfiguration:
    @pytest.fixture()
    def sut(self) -> Configuration:
        return Configuration()

    def test_from_dict(self, sut: Configuration):
        # arrange
        value = 1
        dummy_dict = {"key": value}

        # act
        sut.from_dict(dummy_dict)

        # arrange
        assert sut.key == value
