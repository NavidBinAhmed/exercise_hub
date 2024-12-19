import unittest
from exercise_hub.DSA_2_Array_RandomProblemSolve import reverse_array, sum_element, average_element

class TestArrayFunctions(unittest.TestCase):

    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array([1]), [1])
        self.assertEqual(reverse_array([]), [])

    def test_sum_element(self):
        self.assertEqual(sum_element([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_element([0, 0, 0]), 0)
        self.assertEqual(sum_element([-1, -2, -3]), -6)

    def test_average_element(self):
        self.assertAlmostEqual(average_element([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(average_element([5, 5, 5, 5]), 5.0)
        self.assertAlmostEqual(average_element([1]), 1.0)

if __name__ == '__main__':
    unittest.main()