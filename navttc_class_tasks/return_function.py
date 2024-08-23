# def add():
#     a = 5
#     b = 6
#     return a + b
#
#
# result=(add())
# def sub(result):
#     a=20
#     return a-result
# subtrac=sub(result)
# print(subtrac)



















# def add():
#     a=5
#     b=6
#     c=a+b
#     if c==11:
#         return True
#     print("hello")
#

# def happy_new_year(wishes=True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#
#     return
#     print("Happy New Year!")
# print(happy_new_year())


# def happy_new_year(wishes=True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#
#     print("Happy New Year!")
#
# print(happy_new_year())
#############33


# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#     else:
#             return False
# n=int(input("enetr the number for n"))
# result= strange_function(n)
# print( result)

# def list_sum(lst):
#     s = 0
#
#     for elem in lst:
#         s += elem
#
#     return s
#
#
# print(list_sum([5, 4, 3]))

# #########################
#   $$$$$$$$$$$$$$$$$leap year$$$$$$$$$$$$$$$$$$$$$$$$$$
# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
#
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "->", end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

#############the month  and year###########
# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     if month < 1 or month > 12 or year < 1:
#         return None  # Return None if the input is invalid

#     days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_year_leap(year):
#         return 29
#     else:
#         return days_of_month[month - 1]
#
# # Test cases
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end=" ")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")


##########################the 2 function to find leap year chk test cases#########################

# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     if month < 1 or month > 12 or year < 1:
#         return None  # Return None if the input is invalid
#
#     C = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_year_leap(year):
#         return 29
#     else:
#         return C[month - 1]  # Corrected to use 'C' list
#
# test_cases = [(1900, 2, 28), (2000, 2, 29), (2016, 0, 30), (0, 6, 30)]
# for year, month, result in test_cases:
#     result_of_days = days_in_month(year, month)
#     if result_of_days == result:
#         print(f"{year}-{month}: {result_of_days} -> OK")
#     else:
#         print(f"The year is {year}, the month is {month}, the result is {result_of_days} (expected: {result})")

##############################3 function to kind leap year##########################

def is_year_leap(year):
    # Returns True if the year is a leap year, otherwise False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Returns the number of days in a given month of a given year
    if month < 1 or month > 12 or year < 1:
        return None  # Return None if the input is invalid

    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_of_month[month - 1]

def day_of_year(year, month, day):
    # Returns the day number in the year for a given date, or None if invalid
    if month < 1 or month > 12 or year < 1 or day < 1:
        return None  # Invalid date

    days_in_this_month = days_in_month(year, month)
    if day > days_in_this_month:
        return None  # Invalid day for the given month

    day_number = 0
    for m in range(1, month):
        day_number += days_in_month(year, m)

    day_number += day
    return day_number

# Testing the functions
print(day_of_year(2000, 12, 31))  # Expected output: 366 (since 2000 is a leap year)

# Additional test cases
print(day_of_year(2024, 3, 1))
print(day_of_year(2023, 3, 1))
print(day_of_year(2024, 2, 29))
print(day_of_year(2023, 2, 29))
print(day_of_year(0, 12, 31))
print(day_of_year(2024, 13, 1))
print(day_of_year(2024, 4, 31))  
