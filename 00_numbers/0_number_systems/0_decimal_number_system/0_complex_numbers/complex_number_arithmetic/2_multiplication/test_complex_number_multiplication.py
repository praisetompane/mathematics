def test_multiply_complex_numbers():
    z = 1 + 2j
    w = 3 - 5j

    product = z * w
    print(product)
    assert product == (13 + 1j)
