from str2date import str2date
from datetime import date
from datetime import timedelta
from string_checker import string_checker
from smart_number_checker import smart_number_checker
from data_check_core import str2date2
import pandas as pd
import math
from data_check_core import bool_checker
from data_check_core import remove_char_from_number

dates = ['1953-10-12', '1980-12-16', '1954-01-20', '1961-10-03', '1977-05-13', '1966-09-16', '1976-02-23', '1962-03-30', '1973-03-10', None]
NewCustomerList = pd.read_csv("NewCustomerList.csv")
CustomerDemographic = pd.read_csv("CustomerDemographics.csv")
Transactions = pd.read_csv("Transactions.csv")

test_numbers = pd.read_csv("test_numbers.csv")

"""
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
    if isinstance(string_checker(string, {}), bool):
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



column_of_numbers = [0, 1 , 5, 9,None, 8, ' ']

for number in column_of_numbers:
    print(smart_number_checker(number))


print(test_numbers.head(20))



print(math.isnan("Is this a number?"))

tracker = []
errors = []
counter = -1

for number in test_numbers["second_number"]:
    counter += 1
    if smart_number_checker(number) == True:
        pass
    else:
        tracker.append(counter)
        errors.append(number)


print(tracker)
print(errors)

myString = ""

print(isinstance(myString, str))


def column_str_check(col):
    tracker = []
    string = []
    counter = -1
    for element in col:
        counter += 1
        if isinstance(element, str) is False:
            tracker.append(counter)
            string.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, string

last_name_check = column_str_check(NewCustomerList["last_name"])
print("Result for last name check:")
print(last_name_check[0])
print(last_name_check[1])


last_names = NewCustomerList["last_name"]
i = 0
for name in last_names:
    print(f"{i}  {name}")
    i += 1

print(type(last_names[12]))


def datetime_check_format(col):
    tracker = []
    false_dates = []
    true_dates = []
    counter = -1
    for element in col:
        counter +=1
        if isinstance(str2date(element), date):
            true_dates.append(str2date(element))
        else:
            tracker.append(counter)
            false_dates.append(str2date(element))

    return tracker, false_dates, true_dates




def datetime_check_logic(col):
    tracker = []
    illogical_dates = []
    counter = -1
    criteria_old = timedelta(days=36500)
    criteria_young = timedelta(days=365*18)
    for element in col:
        counter += 1
        if date.today() - element < criteria_young or date.today() - element > criteria_old:
            illogical_dates.append(element)
            tracker.append(counter)

    if len(tracker) == 0:
        return "dates are logical."
    else:
        return tracker, illogical_dates


def checking_numbers(col):
    tracker = []
    errors = []
    counter = -1
    for element in col:
        counter += 1
        if smart_number_checker(element) == True:
            pass
        else:
            tracker.append(counter)
            errors.append(element)
    if len(tracker) == 0:
        return "column is ok"
    else:
        return tracker, errors


print("###################################################################")
print("")
print("Starting check of demographic data")
print("")
print("###################################################################")

DOB_tracker_CD, DOB_false_dates_CD, DOB_true_dates_CD = datetime_check_format(CustomerDemographic["DOB"])
print("Result of DOB check:")
print(DOB_tracker_CD)
print(DOB_false_dates_CD)

print(DOB_true_dates_CD)

DOB_logic_tracker_CD, DOB_illogical_dates_CD = datetime_check_logic(DOB_true_dates_CD)
print(DOB_illogical_dates_CD)
print(DOB_logic_tracker_CD)

for element in DOB_true_dates_CD:
    print(f"{element}, {type(element)}")


print("###################################################################")
print("")
print("Starting check of new customer list data")
print("")
print("###################################################################")

DOB_tracker_NC, DOB_false_dates_NC, DOB_true_dates_NC = datetime_check_format(NewCustomerList["DOB"])
print("Result of DOB check:")
print(DOB_tracker_NC)
print(DOB_false_dates_NC)

#print(DOB_true_dates_NC)


for element in DOB_true_dates_NC:
    print(f"{element}, {type(element)}")
print("#######################")
print(len(DOB_true_dates_NC))
print(type(DOB_true_dates_NC))
print(DOB_true_dates_NC)

result = datetime_check_logic(DOB_true_dates_NC)
print(result)

property_valuation_check = checking_numbers(NewCustomerList["property_valuation"])
print("Result of property valuation check")
print(property_valuation_check)

def datetime_check_format2(col):
    tracker = []
    false_dates = []
    true_dates = []
    counter = -1
    for element in col:
        counter +=1
        if isinstance(str2date2(element), date):
            true_dates.append(str2date2(element))
        else:
            tracker.append(counter)
            false_dates.append(str2date(element))

    return tracker, false_dates, true_dates



dates_list = []

for day in Transactions["transaction_date"]:
    dates_list.append(str2date2(day))

tracker = -1
for day in dates_list:
    tracker += 1
    print(f"{day}, {tracker}, {type(day)}")
    

def datetime_check_format2(col):
    tracker = []
    false_dates = []
    correct_dates = []
    counter = -1
    for day in col:
        counter += 1
        if str2date2(day) == type(date):
            correct_dates.append(str2date2(day))
        else:
            false_dates.append(day)
            tracker.append(counter)
    return correct_dates, false_dates, tracker

Transaction_dates_check, false_dates, tracker = datetime_check_format2(Transactions["transaction_date"])
print("Result of Transaction dates check:")
print(tracker)
print(false_dates)



online_orders = []
missing_data = []
tracker = []
counter = -1
for element in Transactions["online_order"]:
    counter +=1
    if bool_checker(element) == True:
        online_orders.append(int(element))
    else:
        missing_data.append(element)
        tracker.append(counter)
        print(f"{element}, {type(element)}, index: {counter}")

print(f"Length of tracker: {len(tracker)}")

"""
list_of_prices = []
for element in Transactions["standard_cost"]:
    list_of_prices.append(remove_char_from_number(element, "$"))

for price in list_of_prices:
    print(f"{price}, {type(price)}")

