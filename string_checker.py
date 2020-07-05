def string_checker(string: str,unaccepted_set: set):
    if isinstance(string, str) is False or string in unaccepted_set:
        return string
    else:
        return True