def multiply(factor_1, factor_2):

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


print(multiply(+1, +2))  # 2
print(multiply(-1, +2))  # -2
print(multiply(-1, -2))  # 2
