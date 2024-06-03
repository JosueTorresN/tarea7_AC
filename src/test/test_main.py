from src.main import suma, resta, multiplcacion, division
import pytest

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 4), (0, 0, 0), (-1, 1, 0), (0, -1, -1), (-1, -1, -2)])
def test_sum(input_a, input_b, expected_result):
    assert suma(input_a, input_b) == expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 0), (0, 0, 8), (-1, 1, -2), (0, -1, 1), (-1, -1, -5)])
def test_sum_error(input_a, input_b, expected_result):
    assert suma(input_a, input_b) != expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 0), (0, 0, 0), (-1, 1, -2), (0, -1, 1), (-1, -1, 0)])
def test_subtract(input_a, input_b, expected_result):
    assert resta(input_a, input_b) == expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 4), (0, 0, 3), (-1, 1, -1), (0, -1, 0), (-1, -1, 1)])
def test_subtract_error(input_a, input_b, expected_result):
    assert resta(input_a, input_b) != expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 4), (0, 0, 0), (-1, 1, -1), (0, -1, 0), (-1, -1, 1)])
def test_multiply(input_a, input_b, expected_result):
    assert multiplcacion(input_a, input_b) == expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 5), (0, 0, 1), (-1, 1, 1), (0, -1, 2), (-1, -1, 0)])
def test_multiply_error(input_a, input_b, expected_result):
    assert multiplcacion(input_a, input_b) != expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 1), (0, 0, "error"), (-1, 1, -1), (0, -1, 0), (-1, -1, 1)])
def test_divide(input_a, input_b, expected_result):
    assert division(input_a, input_b) == expected_result

@pytest.mark.parametrize("input_a, input_b, expected_result", [(2, 2, 8), (9, 0, 8), (-1,- 1, -1), (0, -1, "error"), (-1, -2, 2)])
def test_divide_error(input_a, input_b, expected_result):
    assert division(input_a, input_b) != expected_result