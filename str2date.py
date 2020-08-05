import datetime


def str2date(string: str):
    try:
        datetime_holder = datetime.datetime.strptime(string, "%Y-%m-%d")
        return datetime_holder.date()
    except ValueError:
        return string
    except TypeError:
        return string
