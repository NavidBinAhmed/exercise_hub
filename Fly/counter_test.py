import unittest
from io import StringIO
import sys

def test_counter(beginner=1, finisher=5):
    step = 1 if beginner <= finisher else -1
    for i in range(beginner, finisher + step, step):
        print(i)

class TestPrintRange(unittest.TestCase):
    
    def test_for_no_given_range_default(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "1\n2\n3\n4\n5\n")

    def test_for_single_argument(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter(1, 3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "1\n2\n3\n")

    def test_for_two_equal_arguments(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter(3, 3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "3\n")

    def test_for_ascending_range(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter(3, 5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "3\n4\n5\n")

    def test_for_descending_range(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter(5, 3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "5\n4\n3\n")

    def test_for_negative_to_positive_range(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        test_counter(-2, 3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "-2\n-1\n0\n1\n2\n3\n")

if __name__ == "__main__":
    unittest.main()