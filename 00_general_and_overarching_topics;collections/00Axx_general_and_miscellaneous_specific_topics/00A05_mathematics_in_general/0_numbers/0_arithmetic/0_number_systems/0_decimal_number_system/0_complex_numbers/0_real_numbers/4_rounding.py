from enum import Enum


class PlaceValue(Enum):
    THOUSANDS = 0
    HUNDREDS = 0
    TENS = 0
    ONES = 0


def round(value: float, place_value: PlaceValue) -> float | int:
    """
    An implementation of the  General Nearest Rounding algorithm.

    Args:
        value (float): The number to round.
        place_value (PlaceValue): The required decimal point precision.

    Returns:
        float | int: The rounded number.
    """
    """
        flow:
        value_array = str(value).split
        number_length = len(value_array)
        if number_length >= 4 and place_value == PlaceValue.THOUSANDS:
            return value * 1000
        if number_length >= 3 and place_value == PlaceValue.HUNDREDS:
            return value * 100
        if number_length >= 2 and place_value == PlaceValue.TENS:
        return none
    """
    return 0
