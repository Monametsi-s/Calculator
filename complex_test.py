import pytest
from lab1_complex import parse_complex, cadd, csub, cmul, cdiv

def test_parse_complex_basic():
    assert parse_complex("3") == 3 + 0j
    assert parse_complex("1+2j") == 1 + 2j
    assert parse_complex("1+2i") == 1 + 2j
    assert parse_complex(" -3-4i ") == -3 - 4j

def test_add_sub_mul_div():
    a = parse_complex("1+2j")
    b = parse_complex("3-4j")
    assert cadd(a, b) == (4 - 2j)
    assert csub(a, b) == (-2 + 6j)
    assert cmul(a, b) == (11 + 2j)  # (1+2j)*(3-4j) = 3 - 4j + 6j -8j^2 = 3+2j+8 = 11+2j
    assert cdiv(a, b) == pytest.approx((1+2j) / (3-4j))

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        cdiv(1 + 0j, 0 + 0j)

def test_invalid_parse():
    with pytest.raises(ValueError):
        parse_complex("not-a-number")