import pandas as pd
from datetime import date
from datetime import timedelta
from data_check_core import str2date
from data_check_core import string_checker
from data_check_core import y_or_n_checker
from data_check_core import smart_number_checker
from data_check_core import str2date2
from data_check_core import bool_checker
from data_check_core import remove_char_from_number

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
"""
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
"""
def gender_check_length(col):
    tracker = []
    false_reports = []
    counter = -1
    for element in col:
        counter += 1
        if y_or_n_checker(element, {"m", "M", "Male", "male", "f", "F", "Female", "female"}):
            pass
        else:
            tracker.append(counter)
            false_reports.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, false_reports


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

def checking_string_in_category(col):
    online_orders = []
    missing_data = []
    tracker = []
    counter = -1
    for element in Transactions["online_order"]:
        counter += 1
        if bool_checker(element) == True:
            online_orders.append(int(element))
        else:
            missing_data.append(element)
            tracker.append(counter)
            # print(f"{element}, {type(element)}, index: {counter}")
    return online_orders, missing_data, tracker




def checking_approved_or_no(col):
    tracker = []
    false_reports = []
    counter = -1
    for element in col:
        counter += 1
        if y_or_n_checker(element, {"Approved", "APPROVED", "approved", "Cancelled", "CANCELLED", "cancelled"}):
            pass
        else:
            tracker.append(counter)
            false_reports.append(element)
    if len(tracker) == 0:
        return "column is ok."
    else:
        return tracker, false_reports

def fix_numbers(col):
    tracker = []
    erroneous_fields = []
    converted_numbers = []
    counter = -1
    for element in col:
        counter += 1
        if remove_char_from_number(element, "$"):
            converted_numbers.append(remove_char_from_number(element, "$"))
        else:
            erroneous_fields.append(element)
            tracker.append(counter)
    return converted_numbers, erroneous_fields, tracker



print("###################################################################")
print("")
print("Starting check of demographic data")
print("")
print("###################################################################")

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

print("###################################################################")
print("")
print("Starting check of address data")
print("")
print("###################################################################")

customer_id_check = checking_numbers(CustomerAddress["customer_id"])
print("Result for ID check:")
print(customer_id_check)

address_check = string_for_category(CustomerAddress["address"])
print("Result for address check:")
print(address_check)

postcode_check = checking_numbers(CustomerAddress["postcode"])
print("Result for postcode check:")
print(postcode_check)

state_check = string_for_category(CustomerAddress["state"])
print("Result for state check:")
print(state_check)

country_check = string_for_category(CustomerAddress["country"])
print("Result for country check:")
print(country_check)

property_valuation_check = checking_numbers(CustomerAddress["property_valuation"])
print("Result of property valuation check")
print(property_valuation_check)

print("###################################################################")
print("")
print("Starting check of new customer list data")
print("")
print("###################################################################")

first_name_check = column_str_check(NewCustomerList["first_name"])
print("Result for first name check:")
print(first_name_check)

last_name_check = column_str_check(NewCustomerList["last_name"])
print("Result for last name check:")
print(last_name_check[0])
print(last_name_check[1])

gender_check = gender_check_length(NewCustomerList["gender"])
print("Result for gender check:")
print(gender_check[0])
print(gender_check[1])

bike_purchase_history_check = checking_numbers(NewCustomerList["past_3_years_bike_related_purchases"])
print("Result for purchase history check:")
print(bike_purchase_history_check)

DOB_tracker, DOB_false_dates, DOB_true_dates = datetime_check_format(NewCustomerList["DOB"])
print("Result of DOB check:")
print(DOB_tracker)
print(DOB_false_dates)

DOB_logic_result = datetime_check_logic(DOB_true_dates)
print(DOB_logic_result)

job_title_check = column_str_check(NewCustomerList["job_title"])
print("Result for job_title check:")
print(job_title_check[0])
print(job_title_check[1])

job_industry_category = string_for_category(NewCustomerList["job_industry_category"])
print("Result for job_industry_category:")
print(job_industry_category[0])
print(job_industry_category[1])

wealth_segment_category = string_for_category(NewCustomerList["wealth_segment"])
print("Result for wealth_segment:")
print(wealth_segment_category)

deceased_indicator = checking_yes_or_no(NewCustomerList["deceased_indicator"])
print("Result for deceased_indicator:")
print(deceased_indicator)

owns_car = checking_yes_or_no(NewCustomerList["owns_car"])
print("Result for owns_car:")
print(owns_car)

tenure_check = checking_numbers(NewCustomerList["tenure"])
print("Result for tenure:")
print(tenure_check)

address_check = string_for_category(NewCustomerList["address"])
print("Result for address check:")
print(address_check)

postcode_check = checking_numbers(NewCustomerList["postcode"])
print("Result for postcode check:")
print(postcode_check)

state_check = string_for_category(NewCustomerList["state"])
print("Result for state check:")
print(state_check)

country_check = string_for_category(NewCustomerList["country"])
print("Result for country check:")
print(country_check)

property_valuation_check = checking_numbers(NewCustomerList["property_valuation"])
print("Result of property valuation check")
print(property_valuation_check)

property_valuation_check = checking_numbers(NewCustomerList["Rank"])
print("Result of Rank check")
print(property_valuation_check)

property_valuation_check = checking_numbers(NewCustomerList["Value"])
print("Result of Value check")
print(property_valuation_check)

print("###################################################################")
print("")
print("Starting check of transactions data")
print("")
print("###################################################################")

customer_id_check = checking_numbers(Transactions["transaction_id"])
print("Result for Transaction ID check:")
print(customer_id_check)

customer_id_check = checking_numbers(Transactions["product_id"])
print("Result for Product ID check:")
print(customer_id_check)

customer_id_check = checking_numbers(Transactions["customer_id"])
print("Result for Costumer ID check:")
print(customer_id_check)

Transaction_dates_check, false_dates, tracker = datetime_check_format2(Transactions["transaction_date"])
print("Result of Transaction dates check:")
print(f"There are {len(false_dates)} errors in transaction dates.")

online_order_check, missing_fields, tracker = checking_string_in_category(Transactions["online_order"])
print("Result of Online order check:")
print(f"There are {len(missing_fields)} errors in online order column.")

order_status = checking_approved_or_no(Transactions["order_status"])
print("Result for order_status:")
print(order_status)

tracker, brands  = column_str_check(Transactions["brand"])
print("Result for brands column:")
print(f"There are {len(tracker)} missing entries in brand.")

tracker, product_line = column_str_check(Transactions["product_line"])
print("Result for product_line column:")
print(f"There are {len(tracker)} missing entries in product_line.")

tracker, product_class = column_str_check(Transactions["product_class"])
print("Result for product_class column:")
print(f"There are {len(tracker)} missing entries in product_class.")

tracker, product_size = column_str_check(Transactions["product_size"])
print("Result for product_size column:")
print(f"There are {len(tracker)} missing entries in product_size.")

list_price_check = checking_numbers(Transactions["list_price"])
print("Result for list_price:")
print(list_price_check)

standard_cost_check, errors, tracker = fix_numbers(Transactions["standard_cost"])
print("Result of standard_cost check:")
print(f"There are {len(standard_cost_check)} correctly converted prices.")
print(f"There are {len(tracker)} errors in standard_cost column.")

for i in range(len(tracker)):
    print(f"{errors[i]}, {tracker[i]}")

product_first_sold_errors, tracker = checking_numbers(Transactions["product_first_sold_date"])
print("Result for product_first_sold_date check:")
print(f"There are {len(product_first_sold_errors)} errors in the column.")

for i in range(len(tracker)):
    print(f"{tracker[i]}, {product_first_sold_errors[i]}")