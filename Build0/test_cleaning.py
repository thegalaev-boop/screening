from cleaning import parse_float, to_arrhenius_point
import pytest
def test_cleaning():
    assert parse_float('N/A') == None
    assert parse_float('0') == 0
    assert parse_float('1.40E-2') == 0.014
    assert to_arrhenius_point(25, 0.012) == pytest.approx((3.35, -1.92), abs = 1e-2)