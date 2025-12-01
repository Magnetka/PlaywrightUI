import pytest

@pytest.mark.smoke
def test_smoke_case():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...
