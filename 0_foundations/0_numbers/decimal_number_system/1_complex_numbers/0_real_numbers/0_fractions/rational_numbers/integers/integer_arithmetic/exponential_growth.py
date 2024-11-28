import numpy as np
import numpy.typing as npt


def double_the_previous(n: npt.NDArray):
    return 2**n


def triple_the_previous(n: npt.NDArray):
    return 3**n


def quadruple_the_previous(n: npt.NDArray):
    return 4**n


def quintuple_the_previous(n: npt.NDArray):
    return 5**n


def sextuple_the_previous(n: npt.NDArray):
    return 6**n


def exponential(base: int, iterations) -> npt.NDArray:
    """
    Args:
        iterations(nparray): the number of the current growth cycle.
        base(int): how much you want to multiple(grow) by per iteration.
    Returns:
        nparray: growth results at each iteration
    """
    return base**iterations


numbers = np.arange(1, 6)

print(numbers)
print(double_the_previous(numbers))
print(triple_the_previous(numbers))
print(quadruple_the_previous(numbers))
print(quintuple_the_previous(numbers))
print(sextuple_the_previous(numbers))

print(exponential(2, numbers))
print(exponential(3, numbers))
print(exponential(4, numbers))
print(exponential(5, numbers))
print(exponential(6, numbers))
