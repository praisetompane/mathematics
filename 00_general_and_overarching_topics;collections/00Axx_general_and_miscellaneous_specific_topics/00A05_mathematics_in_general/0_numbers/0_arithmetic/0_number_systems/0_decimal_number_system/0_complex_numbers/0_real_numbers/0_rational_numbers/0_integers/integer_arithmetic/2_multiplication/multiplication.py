def multiply(factor_1: int, factor_2: int) -> int:
    """
    An implementation of the Generalization Multiplication Algorithm.

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
