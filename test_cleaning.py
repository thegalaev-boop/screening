from cleaning import parse_float
def test_parse_float_valid():
    assert parse_float('25.5') == 25.5
    assert parse_float('1.2e-4') == 0.00012
    assert parse_float("N/A") is None
