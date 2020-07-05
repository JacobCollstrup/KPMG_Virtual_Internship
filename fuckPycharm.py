from str2date import str2date
from datetime import date
from string_checker import string_checker
dates = ['1953-10-12', '1980-12-16', '1954-01-20', '1961-10-03', '1977-05-13', '1966-09-16', '1976-02-23', '1962-03-30', '1973-03-10', None]

first_date = str2date(dates[0])
print(first_date)
print(type(first_date))

correct_dates = []
wrong_dates = []
for element in dates:
    if isinstance(str2date(element), date):
        correct_dates.append(str2date(element))
    else:
        wrong_dates.append(str2date(element))

print(correct_dates)
print(wrong_dates)

print("checking stringchecker...")
strings = ['Mass Customer', 'Mass Customer', 'Mass Customer', 'Mass Customer', 'Affluent Customer', 'High Net Worth', '', 'Affluent Customer', 'Mass Customer', 'Affluent Customer', 'Mass Customer', 'Mass Customer', 'n/a']
false_strings = []
tracker = []
counter = -1
for string in strings:
    counter += 1
    if isinstance(string_checker(string, {"", "n/a", "N/A"}), bool):
        pass
    else:
        false_strings.append(string_checker(string, {"", "n/a", "N/A"}))
        tracker.append(counter)

print(false_strings)
print(tracker)

false_strings = []
tracker = []
counter = -1
for string in strings:
    counter += 1
    if isinstance(string_checker(string, {"", "n/a", "N/A"}), bool):
        pass
    else:
        false_strings.append(string_checker(string, {"", "n/a", "N/A"}))
        tracker.append(counter)

print(false_strings)
print(tracker)

