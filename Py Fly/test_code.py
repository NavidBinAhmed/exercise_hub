import unittest
from typing import List, Union


def sumnum(numbers: List[Union[int, float]]) -> Union[int, float]:
    '''calculating the sum of a list of numbers.
    
    given are arguments and returns as float or int type of numbers in the list'''

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise ValueError("All elements must be integers or numbers!")
    
    summation = 0
    for elements in numbers:
        summation += elements

    return summation

class TestFucntion_sum(unittest.TestCase):

    def test_sum_integers(self):
        self.assertEqual(sumnum([1,2,4]), 7)

    def test_sum_floats(self):
        self.assertEqual(sumnum([1.4, 2.6, 3.0]), 7.0)

    def test_sum_mixed(self):
        self.assertEqual(sumnum([1, 5, 3.5, 2]), 11.5)

    def test_empty_list(self):
        self.assertEqual(sumnum([]), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sumnum([1, '2', 3])

    def test_large_numbers(self):
        self.assertEqual(sumnum([1e10, 1e10]), 2e10)


if __name__ == '__main__':
    unittest.main()

