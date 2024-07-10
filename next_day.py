'''
1. Problem Statement: The Next Day:
Write a Python script to print the date of the next day.

Cases:
    2) If there is no parameter given, find the date for tomorrow.
    3) If a parameter is given, find the date next to that day. The parameter is in YYYYMMDD format.
    4) Assume that YYYY always 4 digits, no leading zero.
 
Hints:
    1) Check the conditions very well.
    2) Beware of the leap year.
'''

from datetime import datetime, timedelta
import sys


def find_next_day(date_str=None):
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            print("invalid date format. Please use YYYYMMDD.")
            return
        
    else:
        date = datetime.now()

    next_day = date + timedelta(days=1)

    return next_day.strftime("%Y%m%d")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_date = sys.argv[1]
        print(find_next_day(input_date))
    else:
        print(find_next_day())

