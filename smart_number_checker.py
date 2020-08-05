import math


def smart_number_checker(number: int or float):
    if math.isnan(number):
        return number
    if isinstance(number, (int, float)) is False:
        return number
    else:
        return True
