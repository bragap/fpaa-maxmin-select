import unittest
from max_min_select import find_max_min

class TestMaxMinSelect(unittest.TestCase):

    def test_single_element(self):
        arr = [5]
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, 5)
        self.assertEqual(max_element, 5)

    def test_two_elements(self):
        arr = [3, 8]
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, 3)
        self.assertEqual(max_element, 8)

    def test_multiple_elements(self):
        arr = [10, 2, 34, 4, 17]
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, 2)
        self.assertEqual(max_element, 34)

    def test_with_negative_numbers(self):
        arr = [-10, -20, -5, 0, 15]
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, -20)
        self.assertEqual(max_element, 15)

    def test_empty_array(self):
        arr = []
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, "Empty array")
        self.assertEqual(max_element, "Empty array")

    def test_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        min_element, max_element = find_max_min(arr)
        self.assertEqual(min_element, 1)
        self.assertEqual(max_element, 1)

if __name__ == '__main__':
    unittest.main()
