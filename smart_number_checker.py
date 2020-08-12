import math


def smart_number_checker(input: int or float or str):
    try:
        if isinstance(input, str):
            input = input.replace(",", ".")

        number = float(input)
        if math.isnan(number):
            return number
        if isinstance(number, (int, float)) is False:
            return number
        else:
            return True

    except ValueError:
        print("This is not a number!")