from multiplication import multiply


def test_same_sign_positive():
    assert multiply(+1, +2) == 2


def test_different_signs():
    assert multiply(-1, +2) == -2


def test_same_sign_negative():
    assert multiply(-1, -2) == 2


def test_same_sign_negative_two_digit_number():
    assert multiply(-7, -20) == 140
