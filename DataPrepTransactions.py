import pandas as pd
from datetime import date
from datetime import timedelta
from str2date import str2date
from string_checker import string_checker
from y_or_n_checker import y_or_n_checker
from smart_number_checker import smart_number_checker

CustomerAddress = pd.read_csv("CustomerAddress.csv")
CustomerDemographic = pd.read_csv("CustomerDemographics.csv")
NewCustomerList = pd.read_csv("NewCustomerList.csv")
Transactions = pd.read_csv("Transactions.csv")

def column_int_check(col):
    tracker = []
    errors = []
    counter = -1
    for element in col:
        counter += 1
        if isinstance(element, int) is False:
            tracker.append(counter)
            errors.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, errors

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

def gender_check_length(col):
    tracker = []
    gender = []
    counter = -1
    for element in col:
        counter += 1
        if len(element) < 2:
            tracker.append(counter)
            gender.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, gender


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
    criteria_young = timedelta(days= 365*18)
    for element in col:
        counter += 1
        if date.today() - element < criteria_young or date.today() - element > criteria_old:
            illogical_dates.append(element)
            tracker.append(counter)

    if len(tracker) == 0:
        return "dates are logical."
    else:
        return tracker, illogical_dates


def string_for_category(col):
    tracker = []
    false_strings = []
    counter = -1
    for element in col:
        counter += 1
        if isinstance(string_checker(element, {"", "n/a", "N/A"}), bool):
            pass
        else:
            false_strings.append(string_checker(element, {"", "n/a", "N/A"}))
            tracker.append(counter)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, false_strings

def checking_yes_or_no(col):
    tracker = []
    false_reports = []
    counter = -1
    for element in col:
        counter += 1
        if y_or_n_checker(element, {"yes", "YES", "Yes", "y", "Y", "no", "NO", "No", "n", "N"}):
            pass
        else:
            tracker.append(counter)
            false_reports.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, false_reports

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



customer_id_check = column_int_check(CustomerDemographic["customer_id"])
print("Result for customer ID check:")
print(customer_id_check)

first_name_check = column_str_check(CustomerDemographic["first_name"])
print("Result for first name check:")
print(first_name_check)

last_name_check = column_str_check(CustomerDemographic["last_name"])
print("Result for last name check:")
print(last_name_check[0])
print(last_name_check[1])

gender_check = gender_check_length(CustomerDemographic["gender"])
print("Result for gender check pass 1:")
print(gender_check[0])
print(gender_check[1])

past_3_years_bike_related_purchases = column_int_check(CustomerDemographic["past_3_years_bike_related_purchases"])
print("Result for ast_3_years_bike_related_purchases:")
print(past_3_years_bike_related_purchases)


DOB_tracker, DOB_false_dates, DOB_true_dates = datetime_check_format(CustomerDemographic["DOB"])
print("Result of DOB check:")
print(DOB_tracker)
print(DOB_false_dates)

DOB_logic_tracker, DOB_illogical_dates = datetime_check_logic(DOB_true_dates)
print(DOB_illogical_dates)
print(DOB_logic_tracker)

job_title_check = column_str_check(CustomerDemographic["job_title"])
print("Result for job_title check:")
print(job_title_check[0])
print(job_title_check[1])

job_industry_category = string_for_category(CustomerDemographic["job_industry_category"])
print("Result for job_industry_category:")
print(job_industry_category[0])
print(job_industry_category[1])

wealth_segment_category = string_for_category(CustomerDemographic["wealth_segment"])
print("Result for wealth_segment:")
print(wealth_segment_category)

deceased_indicator = checking_yes_or_no(CustomerDemographic["deceased_indicator"])
print("Result for deceased_indicator:")
print(deceased_indicator)

owns_car = checking_yes_or_no(CustomerDemographic["owns_car"])
print("Result for owns_car:")
print(owns_car)

tenure_check = checking_numbers(CustomerDemographic["tenure"])
print("Result for tenure:")
print(tenure_check[0])
print(tenure_check[1])

