import datetime
import math


# This function checks that the date strings are formatted correctly, according to the specified template.
def str2date(string: str):
    try:
        datetime_holder = datetime.datetime.strptime(string, "%Y-%m-%d")
        return datetime_holder.date()
    except ValueError:
        return string
    except TypeError:
        return string


# This function returns true if the field contains a string. It includes an exclusion set so you can exclude certain
# strings, fx blanks and such.
def string_checker(string: str, unaccepted_set: set):
    if isinstance(string, str) is False or string in unaccepted_set:
        return string
    else:
        return True


# This function is used to check if a field is correctly filled out according to a specific pattern. fx 'Yes' or 'No'.
def y_or_n_checker(string: str, allowed_set: set):
    if string in allowed_set:
        return True
    else:
        return False


# This function checks whether a field contains a number or not. It accepts floats and ints, but not nans.
def smart_number_checker(number: int or float):
    if math.isnan(number):
        return number
    if isinstance(number, (int, float)) is False:
        return number
    else:
        return True
