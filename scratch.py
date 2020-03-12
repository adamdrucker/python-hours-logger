from datetime import datetime
import re

# x = datetime.datetime.now()
# print(x)
# print(x.month,"-",x.day,"-",x.year, sep='') # Prints today's date as MM-DD-YYY

'''
sDate = input("Enter a date: ")
date_format = '%m-%d-%Y'

def date_check(i):
    try:
        datetime.strptime(i, date_format)
        return True
    except ValueError:
        return False

while not date_check(sDate):
    print("Incorrect format, try again.")
    sDate = input("Enter a date: ")
    date_format = '%m-%d-%Y'
    date_check(sDate)
    break
'''

# time_format = "%H:%M"
# sTime = input("Enter a time: ")
#
# def time_check(i):
#     # This checks for the correct format as described below, returns bool
#         try:
#             dt = datetime.strptime(i, "%H:%M")
#             return True
#         except ValueError:
#             return False
#
# def new_time_check(i):
#     checkt = time_check(i)
#     while not checkt:
#         # Checks returned bool and loops for correct input again
#         print("Wrong format entered, try again.")
#         i = input("Enter a time: ")
#         checkt = time_check(i)
#
#     dt = datetime.strptime(i, "%H:%M")
#     d = dt.strftime("%H:%M")
#
#     while i != d:
#         print("Time's do not match")
#         i = input("Enter a time: ")
#
#
# new_time_check(sTime)

# while sTime != d:
#     sTime = input("Enter a time: ")
#     try:
#         print("Wrong format, try again.")
#         dt = datetime.strptime(sTime, "%H:%M")
#         d = dt.strftime("%H:%M")
#     except ValueError:
#         print("value error")
#         continue


# This needs to break apart the input time, first passing the "XX:XX" format check,
#  then make sure that each integer is either zero-padded if single digit or a double
#   digit integer (along with checking that it is a valid time i.e. <24:00

# def time_check(i):
#     try:
#         datetime.strptime(i, "%H:%M")
#         return True
#     except ValueError:
#         return False
#
#
# while not time_check(sTime):
#     print("Incorrect format, try again.")
#     sTime = input("Enter a time: ")
#     # ---
#     time_check(sTime)
#     continue
#
#
# time = f"{hour}:{minute}"
# print(time)

