import unittest
from fields import rectangle, triangle, trapeze


class FieldsTestCase(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 5
        self.h = 2

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 50)

    def test_rectangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            rectangle(5, 'aaa')

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 25)

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(5, 'aaa')

    def test_trapeze_with_correct_values(self):
        result = trapeze(self.a, self.b, self.h)
        self.assertEqual(result, 15)

    def test_trapeze_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            trapeze(5, 'aaa', True)

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()
