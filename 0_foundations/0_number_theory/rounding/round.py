from enum import Enum


class PlaceValue(Enum):
    THOUSANDS = 0
    HUNDREDS = 0
    TENS = 0
    ONES = 0


def round(value: int, place_value: PlaceValue):
    """
        value_array = str(value).split
        number_length = len(value_array)

        if number_length >= 4 and place_value == PlaceValue.THOUSANDS:
            return value * 1000
        if number_length >= 3 and place_value == PlaceValue.HUNDREDS:
            return value * 100
        if number_length >= 2 and place_value == PlaceValue.TENS:
        return none
    """