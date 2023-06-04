import pytest
import os


@pytest.fixture
def demo_dataclass():
    return '/Users/pro/Documents/proj_data/demo_dataclass'


def test_file_exists(demo_dataclass):
    assert os.path.exists(demo_dataclass)


def test_file_is_readable(demo_dataclass):
    assert os.access(demo_dataclass, os.R_OK)
