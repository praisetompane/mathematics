def multiply(factor_1: int, factor_2: int) -> int:
    """
    An implementation of the Generalization Multiplication Algorithm.
        see for specification: 00_numbers/0_number_systems/0_decimal_number_system/0_complex_numbers/0_real_numbers/0_rational_numbers/0_fractions/0_integers/integer_arithmetic/2_multiplication/0_multiplication.txt

    Args:
        factor_1 (int): The first number.
        factor_2 (int): The first number.

    Returns:
        int: The product of the two numbers.
    """

    def result_sign(sum):
        if factor_1 < 0 and factor_2 < 0:  # Signs the same
            return sum
        elif factor_1 > 0 and factor_2 > 0:  # Signs the same
            return sum
        else:  # Signs different
            return -sum

    result = 0
    for _ in range(int(abs(factor_1))):  # Repeated addition, ignoring signs
        result += abs(factor_2)
    return result_sign(result)
