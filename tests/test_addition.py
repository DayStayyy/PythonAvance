import pytest
from PythonAvance.basicFunction import addition, conditional

@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 5, 7), (812, 458421, 459233)])
def test_addition(a, b, expected):
    assert addition(a, b) == expected
