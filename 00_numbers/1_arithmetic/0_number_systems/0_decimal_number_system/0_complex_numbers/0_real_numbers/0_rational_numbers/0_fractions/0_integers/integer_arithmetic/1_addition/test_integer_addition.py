from integer_addition import add_integers


def test_add_same_sign_negative():
    number_1 = -9
    number_2 = -20

    result = add_integers(number_1, number_2)
    assert result == -29


def test_add_same_sign_positive():
    number_1 = 10
    number_2 = 1

    result = add_integers(number_1, number_2)
    assert result == 11


def test_add_different_signs():
    number_1 = 10
    number_2 = -1

    result = add_integers(number_1, number_2)
    assert result == 9


def test_add_zeros():
    number_1 = 0
    number_2 = 0

    result = add_integers(number_1, number_2)
    assert result == 0


def test_add_zero_to_positive():
    number_1 = 0
    number_2 = 90

    result = add_integers(number_1, number_2)
    assert result == 90


def test_add_zero_to_negative():
    number_1 = 0
    number_2 = -89

    result = add_integers(number_1, number_2)
    assert result == -89
