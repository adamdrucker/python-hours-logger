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


def check_time_format(i):
    # This checks for the correct format as described below, returns bool
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

    # Ending time prompt
    print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
    iOutTime = input(f"Enter END time for {iShiftDate}: ")

    while not check_time(iOutTime):
        print("Invalid entry, try again.")
        print("PLEASE BE ADVISED: Times must be formatted in 24-hour notation as HH:MM.")
        iOutTime = input(f"Enter END time for {iShiftDate}: ")
        check_time(iOutTime)

    # Work description
    sDescInput = input("Enter a description: ")

    # Output
    sOutput = f"{sName}|{iShiftDate} {iInTime}|{iShiftDate} {iOutTime}|{sPaycode}|{sBillable}|{sEmergency}|{sDescInput}"
    print(sOutput)  # Output needs TOTAL after iOutTime


main()
