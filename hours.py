# //////////////////////////////////
# // Script to log working hours //
# ////////////////////////////////

import os
from os import path
from datetime import datetime


# Global variables
date_format = "%m-%d-%Y"
time_format = "%H:%M"


# Functions
# ///////////

# Check for valid date and format
def check_date(i):
    try:
        datetime.strptime(i, date_format)
        return True
    except ValueError:
        return False


# This checks for the correct format as described below, returns bool
def check_time_format(i):
    try:
        dt = datetime.strptime(i, "%H:%M")
        return True
    except ValueError:
        return False


def check_time(i):
    checkt = check_time_format(i)
    if not checkt:
        # Checks returned bool from above
        return False
    else:
        dt = datetime.strptime(i, "%H:%M")
        d = dt.strftime("%H:%M")
        # Checks that entered time and formatted time are the same
        if i != d:
            return False
        else:
            return True


# Splits up hour/minute from time inputs
def time_split(x):
    splist = []
    split = x.split(":", 2)
    sphour = split[0]
    spmin = split[1]
    splist.append(sphour)
    splist.append(spmin)
    return splist


# Determine paycode variable
def lunch_hours(i):
    if i == "Y" or i == "y":
        return "LUNCH"
    elif i == "N" or i == "n":
        return "MGHPCC/INTERN"


# Determines .25 based decimal for final submission
def minute_calc(x):
    if 0 <= x <= 14:
        return 0
    elif 15 <= x <= 29:
        return 25
    elif 30 <= x <= 44:
        return 50
    else:
        return 75


def main():

    # Static variables
    sName = "adrucker"
    sBillable = "Y"
    sEmergency = "N"

    # Starting date prompt
    print("PLEASE BE ADVISED: Each entry must be for the same date, and entered in the following "
          "format MM-DD-YYY.")
    iShiftDate = input("Enter the date of your shift: ")
    check_date(iShiftDate)   # Call date check

    while not check_date(iShiftDate):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Each entry must be for the same date, and entered in the following "
              "format MM-DD-YYY.")
        iShiftDate = input("Enter the date of your shift: ")
        check_date(iShiftDate)

    # Lunch time
    sLunch = input("Are these LUNCH hours? (Y/N): ")
    sPaycode = lunch_hours(sLunch)

    # Starting time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iInTime = input(f"Enter START time for {iShiftDate}: ")

    while not check_time(iInTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iInTime = input(f"Enter START time for {iShiftDate}: ")
        check_time(iInTime)

    # Split in-time into hours/minutes
    iInHour = int((time_split(iInTime))[0])
    iInMin = int((time_split(iInTime))[1])

    # Ending time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iOutTime = input(f"Enter END time for {iShiftDate}: ")

    while not check_time(iOutTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iOutTime = input(f"Enter END time for {iShiftDate}: ")
        check_time(iOutTime)

    # Split out-time into hours/minutes
    iOutHour = int((time_split(iOutTime))[0])
    iOutMin = int((time_split(iOutTime))[1])

    # Calculations
    iHours = iOutHour - iInHour

    iMinCalc = iOutMin - iInMin
    if iMinCalc < 0:
        iMinCalc += 60

    if iInMin > iOutMin:
        iHours -= 1

    iMinutes = minute_calc(iMinCalc)
    iTotal = f"{iHours}.{iMinutes}"

    # Work description
    sDescInput = input("Enter a description: ")

    # Output
    sOutput = f"{sName}|{iShiftDate} {iInTime}|{iShiftDate} {iOutTime}|{iTotal}|{sPaycode}|{sBillable}|{sEmergency}|{sDescInput}"
    print(sOutput)

    CORRECT = input("Is the preceding information correct? (Y/N) ").upper()

    while CORRECT == "N":
        print("Please start over then.")
        break

    while CORRECT == "Y":
        f = open(f"timecard_{d}.txt", "a+")
        f.write(f"{sOutput}\n")
        f.close()
        print("Do you want to submit another entry? ")
        break

    START = input("Press [ENTER] to start or 'q' to quit. ")
    if START == "q":
        exit()


# Begin
print("Welcome to the Timecard Logging System.\n"
      "Here you will enter dates and times you've worked. Tasks should be separated and itemized.")
START = input("Press [ENTER] to start or 'q' to quit. ")

# START Windows host systems #-------------------------------------
# d = f"{datetime.now():%m-%d-%Y}"  # Date variable for filename
# dPath = "D:/Documents (HDD)/Script/Python/ts"  # My local destination path
# cPath = os.getcwd()  # Gets current directory
#
# if cPath == dPath:
#     # Create text file in destination if non-existent
#     if not path.exists(f"{dPath}/timecard_{d}.txt"):
#         f = open(f"timecard_{d}.txt", "w+")
#         f.close()
# else:
#     # Change to destination if elsewhere
#     os.chdir(dPath)
#     # Create text file in destination if non-existent
#     if not path.exists(f"{dPath}/timecard_{d}.txt"):
#         f = open(f"timecard_{d}.txt", "w+")
#         f.close()
# END Windows host systems #-------------------------------------

# START Linux host systems #-------------------------------------
d = f"{datetime.now():%m-%d-%Y}"  # Date variable for filename
localUser = os.environ['USER']
dPath = f"/home/{localUser}/Documents/techsquare/Timecards"
cPath = os.getcwd()  # Gets current directory

# If desired destination path above doesn't exist,
# create 'techsquare' & 'Timecards' directories
if not path.exists(dPath):
    os.chdir(f"/home/{localUser}/Documents")
    os.makedirs("techsquare/Timecards")

if cPath == dPath:
    # Create text file in destination if non-existent
    if not path.exists(f"{dPath}/timecard_{d}.txt"):
        f = open(f"timecard_{d}.txt", "w+")
        f.close()
else:
    # Change to destination if elsewhere
    os.chdir(dPath)
    # Create text file in destination if non-existent
    if not path.exists(f"{dPath}/timecard_{d}.txt"):
        f = open(f"timecard_{d}.txt", "w+")
        f.close()
# END Linux host systems #-------------------------------------

while START != "q":
    main()
