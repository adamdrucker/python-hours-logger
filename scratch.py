from datetime import datetime


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

sTime = input("Enter a time: ")
dt = datetime.strptime(sTime, "%H:%M")
hour = dt.strftime("%H")
minute = dt.strftime("%M")

# This needs to break apart the input time, first passing the "XX:XX" format check,
#  then make sure that each integer is either zero-padded if single digit or a double
#   digit integer (along with checking that it is a valid time i.e. <24:00

def time_check(i):
    try:
        datetime.strptime(i, "%H:%M")
        return True
    except ValueError:
        return False


while not time_check(sTime):
    print("Incorrect format, try again.")
    sTime = input("Enter a time: ")
    # ---
    time_check(sTime)
    continue


time = f"{hour}:{minute}"
print(time)

