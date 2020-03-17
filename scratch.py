from datetime import datetime
import re
import os
import os.path
from os import path

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

###

# def minute_calc(x):
#     if 0 <= x <= 14:
#         return 0
#     elif 15 <= x <= 29:
#         return 25
#     elif 30 <= x <= 44:
#         return 50
#     else:
#         return 75
#
#
# in_time = input("Enter start time: ")
# out_time = input("Enter end time: ")
#
# split_in = in_time.split(":", 2)  # splits in_time into two strings separated by colon
# in_hour = int(split_in[0])  # turns in hour into int
# in_min = int(split_in[1])  # turns in min into int
#
# split_out = out_time.split(":", 2)
# out_hour = int(split_out[0])
# out_min = int(split_out[1])
#
# hours = out_hour - in_hour
#
# min_calc = out_min - in_min
# if min_calc < 0:
#     min_calc = min_calc + 60
#
# if in_min > out_min:
#     hours = hours - 1
#
# minutes = minute_calc(min_calc)
# total = f"{hours}.{minutes}"
# print(total)

d = f"{datetime.now():%m-%d-%Y}"

dPath = "D:/Documents (HDD)/Script/Python/ts"
cpath = os.getcwd()  # gets current directory
if cpath == dPath:
    if path.exists(f"{dPath}/timecard_{d}.txt"):
        f = open(f"timecard_{d}.txt", "a+")
        f.write("\nappending info")
        f.close()
    else:
        f = open(f"timecard_{d}.txt", "w+")
        f.write("testing this out, current directory")
        f.close()
else:
    os.chdir(r"D:\Documents (HDD)\Script\Python\ts")
    if path.exists(f"D:/Documents (HDD)/Script/Python/ts/timecard_{d}.txt"):
        f = open(f"timecard_{d}.txt", "a+")
        f.write("\nappending info")
        f.close()
    else:
        f = open(f"timecard_{d}.txt", "w+")
        f.write("testing this out, change directory")
        f.close()

