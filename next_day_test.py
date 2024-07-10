import unittest
from datetime import datetime, timedelta

def find_next_day(date_str = None):
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            return "Invalid date format. Use the given format in the statement."
    else:
        date = datetime.now()

    next_day = date + timedelta(days=1)
    return next_day.strftime("%Y%m%d")
 
''' Test Cases:
1. Handle leap year
2. Handle format error
3. Find next day of the given date or for default case 
'''
class TestNextDay(unittest.TestCase):
    
    def test_with_no_parameter_default(self):
        today = datetime.now()
        expected_next_day = (today + timedelta(days=1)).strftime("%Y%m%d")
        self.assertEqual(find_next_day(), expected_next_day)


    def test_for_leap_year_and_various_date_formats(self):
        self.assertEqual(find_next_day("20240711"), "20240712")
        self.assertEqual(find_next_day("20221231"), "20230101")
        self.assertEqual(find_next_day("20000228"), "20000229")
        self.assertEqual(find_next_day("19991231"), "20000101")
        self.assertEqual(find_next_day("21000228"), "21000301")

    def test_invalid_format(self):
        self.assertEqual(find_next_day("2022-02-28"), "Invalid date format. Use the given format in the statement.")
        self.assertEqual(find_next_day("09072024"), "Invalid date format. Use the given format in the statement.")


if __name__ == "__main__":
    unittest.main()