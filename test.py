import pytest
from app import Calculator

@pytest.fixture()
def calculator():
    return Calculator()

# test case for the add method
def test_add(calculator):
    assert calculator.__add__(2,3) == 5
    assert calculator.__add__(-1,1) == 0
    assert calculator.__add__(0,0) == 0
    assert calculator.__add__(-5,-7) == -12


