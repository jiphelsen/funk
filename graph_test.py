from graph import is_type_or_raise,is_node, Node,Vertex,Graph
import unittest

class TestIsTypeOrRaiseFunction(unittest.TestCase):
    
    def test_valid_string(self):
        # Test with a valid string
        value = "Hello, World!"
        s = "test_string"
        t = str
        self.assertIsNone(is_type_or_raise(value, s, t))

    def test_invalid_type(self):
        # Test with an invalid type
        value = 42  # Integer instead of string
        s = "test_integer"
        t = str
        with self.assertRaises(Exception) as context:
            is_type_or_raise(value, s, t)
        self.assertEqual(str(context.exception), f"{s} needs to be of type {t}.")

    def test_none_value(self):
        # Test with None value
        value = None
        s = "test_none"
        t = str
        with self.assertRaises(Exception) as context:
            is_type_or_raise(value, s, t)
        self.assertEqual(str(context.exception), f"{s} can not be None.")

class TestNodeClass(unittest.TestCase):
    
    def test_node_creation(self):
        # Test creating a node
        node = Node(label="A", value=42)
        self.assertEqual(node.label(), "A")
        self.assertEqual(node.value(), 42)

    def test_set_value_method(self):
        # Test set_value method
        node = Node()
        result = node.set_value(100)
        self.assertEqual(result, 100)
        self.assertEqual(node.value(), 100)

    def test_set_label_method(self):
        # Test set_label method
        node = Node()
        result = node.set_label("B")
        self.assertEqual(result, "B")
        self.assertEqual(node.label(), "B")

    def test_is_node_function(self):
        # Test is_node function
        node = Node()
        self.assertTrue(is_node(node))

    def test_is_not_node_function(self):
        # Test is_node function with a non-Node object
        non_node = "This is not a Node"
        self.assertFalse(is_node(non_node))

if __name__ == '__main__':
    unittest.main()
