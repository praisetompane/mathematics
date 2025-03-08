def test_subtract_complex_numers():
    w = 1 + 2j
    z = 3 - 5j

    difference = w - z
    assert difference == (-2 + 7j)
