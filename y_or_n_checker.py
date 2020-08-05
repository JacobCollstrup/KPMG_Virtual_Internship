def y_or_n_checker(string: str, allowed_set: set):
    if string in allowed_set:
        return True
    else:
        return False
