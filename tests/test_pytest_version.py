import pytest


class TestPytestVersion:
    def test_pytest_version_is_correct(self):
        assert pytest.__version__ == "6.2.4"
