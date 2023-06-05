import pytest
from statistics import calculate_statistics

def test_calculate_statistics():
    numbers = [1, 2, 3, 4, 5]
    mean, std_deviation = calculate_statistics(numbers)
    assert mean == 3.0
    assert std_deviation == pytest.approx(1.414, abs=1e-3)