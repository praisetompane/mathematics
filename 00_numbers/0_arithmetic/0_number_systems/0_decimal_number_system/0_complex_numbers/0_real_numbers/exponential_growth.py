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


def exponential(base: int, iterations: npt.NDArray) -> npt.NDArray:
    """Explore exponential growth with variations in base.

    Args:
        base (int): The number of the current growth cycle.
        iterations (npt.NDArray): How much you want to multiple(grow) by per iteration.

    Returns:
        npt.NDArray: growth results at each iteration
    """
    return base**iterations


powers = np.arange(1, 9)
print(f"base numbers {powers}")
for base in range(10):
    print(exponential(base, powers))
