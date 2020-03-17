# //////////////////////////////////
# // Script to log working hours //
# ////////////////////////////////

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


# Determine paycode variable
def lunch_hours(i):
    if i == "Y" or i == "y":
        return "LUNCH"
    elif i == "N" or i == "n":
        return "MGHPCC"


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
    spInTime = iInTime.split(":", 2)
    iInHour = int(spInTime[0])
    iInMin = int(spInTime[1])

    # Ending time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iOutTime = input(f"Enter END time for {iShiftDate}: ")

    while not check_time(iOutTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iOutTime = input(f"Enter END time for {iShiftDate}: ")
        check_time(iOutTime)

    # Split out-time into hours/minutes
    spOutTime = iOutTime.split(":", 2)
    iOutHour = int(spOutTime[0])
    iOutMin = int(spOutTime[1])

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
    print(sOutput)  # Output needs TOTAL after iOutTime


main()
