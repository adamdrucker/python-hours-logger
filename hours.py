# //////////////////////////////////
# // Script to log working hours //
# ////////////////////////////////

from datetime import datetime

# Global variables
date_format = "%m-%d-%Y"
time_format = "%H:%M"


# Functions
# ///////////


def check_date(i):
    # Check for valid date and format
    try:
        datetime.strptime(i, date_format)
        return True
    except ValueError:
        return False


def check_time(i):
    # Check for valid time and format
    # This needs to be adjusted, see scratch.py
    try:
        datetime.strptime(i, time_format)
        return True
    except ValueError:
        return False


def lunch_hours(i):
    # Determine paycode variable
    if i == "Y" or i == "y":
        return "LUNCH"
    elif i == "N" or i == "n":
        return "MGHPCC"


def main():

    # Static variables
    sName = "adrucker"
    sBillable = "Y"
    sEmergency = "N"

    # Starting date prompt
    print("PLEASE BE ADVISED: Each entry must be for the same date, and entered in the following"
          "format MM-DD-YYY.")
    iShiftDate = input("Enter the date of your shift: ")
    check_date(iShiftDate)   # Call date check

    while not check_date(iShiftDate):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Each entry must be for the same date, and entered in the following"
              "format MM-DD-YYY.")
        iShiftDate = input("Enter the date of your shift: ")
        check_date(iShiftDate)
        continue

    # Lunch time
    sLunch = input("Are these LUNCH hours? (Y/N): ")
    sPaycode = lunch_hours(sLunch)

    # Starting time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iInTime = input(f"Enter START time for {iShiftDate}: ")
    check_time(iInTime)     # Call time check

    while not check_time(iInTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iInTime = input(f"Enter START time for {iShiftDate}: ")
        check_time(iInTime)
        continue

    # Ending time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iOutTime = input(f"Enter END time for {iShiftDate}: ")
    check_time(iOutTime)

    while not check_time(iOutTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iOutTime = input(f"Enter END time for {iShiftDate}: ")
        check_time(iOutTime)
        continue

    # Work description
    sDescInput = input("Enter a description: ")

    # Output
    sOutput = f"{sName}|{iShiftDate} {iInTime}|{iShiftDate} {iOutTime}|{sPaycode}|{sBillable}|{sEmergency}|{sDescInput}"
    print(sOutput)  # Output needs TOTAL after iOutTime


main()
