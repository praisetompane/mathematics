def facts():
    """
    computes and prints basic addition facts up to 10
    """
    total_numbers = 11
    print("identity sum")
    for i in range(total_numbers):
        print(f"{i} + {i} = {i + i}")

    print("adjacent sum")
    for i in range(total_numbers - 1):
        print(f"{i} + {i + 1} = {i + (i + 1)}")

    print("all possible combinations")
    # can be halved due commutative law of addition
    for i in range(total_numbers):
        for j in range(i, total_numbers):
            print(f"{i} + {j} = {i + j}")


if __name__ == "__main__":
    facts()
