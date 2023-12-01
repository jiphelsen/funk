import unittest
from type_utils import is_type_or_raise,check_type_mapping

class TestIsTypeOrRaise(unittest.TestCase):

    def test_valid_type(self):
        value = 42
        name = "example_value"
        expected_type = int
        result = is_type_or_raise(value, name, expected_type)
        self.assertIsNone(result)

    def test_none_value(self):
        value = None
        name = "example_value"
        expected_type = int
        with self.assertRaises(ValueError) as context:
            is_type_or_raise(value, name, expected_type)
        self.assertEqual(str(context.exception), f"{name} cannot be None.")

    def test_invalid_type(self):
        value = "not_an_integer"
        name = "example_value"
        expected_type = int
        with self.assertRaises(TypeError) as context:
            is_type_or_raise(value, name, expected_type)
        self.assertEqual(str(context.exception), f"{name} must be of type {expected_type.__name__}.")




if __name__ == '__main__':
    unittest.main()
