from graph import is_vertex,is_type_or_raise,is_node, Node,Vertex,Graph,is_set
import unittest
class TestTypeFunctions(unittest.TestCase):
    def setUp(self):
        # Create a Node instance for testing
        self.node = Node(label="TestLabel", value="TestValue")
    def test_is_node(self):
        self.assertTrue(is_node(self.node))
        self.assertFalse(is_node("NotANode"))

    def test_is_vertex(self):
        node1 = Node(label="Node1Label", value="Node1Value")
        node2 = Node(label="Node2Label", value="Node2Value")

        vertex = Vertex(head=node1, tail=node2)

        self.assertTrue(is_vertex(vertex))
        self.assertFalse(is_vertex(node1))
        self.assertFalse(is_vertex("NotAVertex"))

    def test_is_set(self):
        nodes_set = {Node(label="Node1Label", value="Node1Value"), Node(label="Node2Label", value="Node2Value")}

        not_a_set = ["Node1Label", "Node2Label"]

        self.assertTrue(is_set(nodes_set))
        self.assertFalse(is_set(not_a_set))
        self.assertFalse(is_set("NotASet"))

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

class TestNode(unittest.TestCase):
    def setUp(self):
        # Create a Node instance for testing
        self.node = Node(label="TestLabel", value="TestValue")

    def test_initialization(self):
        self.assertEqual(self.node.label(), "TestLabel")
        self.assertEqual(self.node.value(), "TestValue")

    def test_set_value(self):
        new_value = self.node.set_value("NewTestValue")
        self.assertEqual(new_value, "NewTestValue")
        self.assertEqual(self.node.value(), "NewTestValue")

    def test_set_label(self):
        new_label = self.node.set_label("NewTestLabel")
        self.assertEqual(new_label, "NewTestLabel")
        self.assertEqual(self.node.label(), "NewTestLabel")
        
    def test_node_equality(self):
        node1 = Node(label="Label1", value="Value1")
        node2 = Node(label="Label1", value="Value1")
        node3 = Node(label="Label2", value="Value2")

        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node2, node3)

    def test_node_hashability(self):
        node1 = Node(label="Label1", value="Value1")
        node2 = Node(label="Label1", value="Value1")
        node3 = Node(label="Label2", value="Value2")

        # Nodes with equal label and value should have the same hash
        self.assertEqual(hash(node1), hash(node2))
        
        # Nodes with different label or value may have different hashes
        self.assertNotEqual(hash(node1), hash(node3))
    def test_str_method(self):
        expected_str = "(value=TestValue, label=TestLabel)"
        actual_str = str(self.node)
        self.assertEqual(actual_str, expected_str)


class TestVertex(unittest.TestCase):
    def setUp(self):
        # Create two Node instances for testing
        self.node1 = Node(label="Node1Label", value="Node1Value")
        self.node2 = Node(label="Node2Label", value="Node2Value")

        # Create a Vertex instance for testing
        self.vertex = Vertex(head=self.node1, tail=self.node2)

    def test_initialization(self):
        self.assertEqual(self.vertex.head(), self.node1)
        self.assertEqual(self.vertex.tail(), self.node2)

    def test_set_head(self):
        new_head = Node(label="NewHeadLabel", value="NewHeadValue")
        updated_head = self.vertex.set_head(new_head)
        self.assertEqual(updated_head, new_head)
        self.assertEqual(self.vertex.head(), new_head)

    def test_set_tail(self):
        new_tail = Node(label="NewTailLabel", value="NewTailValue")
        updated_tail = self.vertex.set_tail(new_tail)
        self.assertEqual(updated_tail, new_tail)
        self.assertEqual(self.vertex.tail(), new_tail)

    def test_nodes(self):
        node_set = self.vertex.nodes()
        self.assertEqual(node_set, {self.node1, self.node2})

    def test_is_loop(self):
        self.assertFalse(self.vertex.is_loop())

        # Create a loop (head and tail nodes are the same)
        loop_vertex = Vertex(head=self.node1, tail=self.node1)
        self.assertTrue(loop_vertex.is_loop())

    def test_is_vertex(self):
        self.assertTrue(is_vertex(self.vertex))
        self.assertFalse(is_vertex("NotAVertex"))

class TestGraph(unittest.TestCase):
    def test_graph_initialization(self):
        # Test initialization with nodes and vertices
        node1 = Node(label="Node1Label", value="Node1Value")
        node2 = Node(label="Node2Label", value="Node2Value")

        vertex = Vertex(head=node1, tail=node2)

        graph = Graph(nodes={node1, node2}, vertices=[vertex])

        self.assertEqual(graph.nodes(), {node1, node2})
        self.assertEqual(graph.vertices(), [vertex])

    def test_add_node(self):
        # Test adding a node to the graph
        graph = Graph()

        node = Node(label="NewNodeLabel", value="NewNodeValue")
        graph.add_node(node)

        self.assertEqual(graph.nodes(), {node})

    def test_add_vertex(self):
        # Test adding a vertex to the graph
        node1 = Node(label="Node1Label", value="Node1Value")
        node2 = Node(label="Node2Label", value="Node2Value")

        graph = Graph(nodes={node1, node2})

        vertex = Vertex(head=node1, tail=node2)
        graph.add_vertex(vertex)

        self.assertEqual(graph.vertices(), [vertex])

    def test_invalid_vertex_addition(self):
        # Test adding a vertex with nodes not in the graph
        node1 = Node(label="Node1Label", value="Node1Value")
        node2 = Node(label="Node2Label", value="Node2Value")

        graph = Graph(nodes={node1})

        invalid_vertex = Vertex(head=node1, tail=node2)

        with self.assertRaises(Exception) as context:
            graph.add_vertex(invalid_vertex)

        self.assertEqual(
            str(context.exception),
            "The new vertex must only be connected with nodes within the graph."
        )
    def test_invalid_node_type(self):
        # Test initialization with invalid node type
        with self.assertRaises(Exception) as context:
            graph = Graph(nodes="NotASet")

        self.assertEqual(
            str(context.exception),
            "Nodes needs to be of type set."
        )

    def test_invalid_node_in_nodes(self):
        # Test initialization with a non-Node element in nodes
        invalid_node = "NotANode"

        with self.assertRaises(Exception) as context:
            graph = Graph(nodes={invalid_node})

        self.assertEqual(
            str(context.exception),
            "All values in nodes need to be of type Node."
        )

    def test_invalid_vertex_type(self):
        # Test initialization with invalid vertex type
        invalid_vertex = "NotAVertex"

        with self.assertRaises(Exception) as context:
            graph = Graph(vertices=[invalid_vertex])

        self.assertEqual(
            str(context.exception),
            "All values in vertices need to be of type Vertex."
        )

    def test_vertices_not_connected_to_graph_nodes(self):
        # Test initialization with vertices not connected to graph nodes
        node1 = Node(label="Node1Label", value="Node1Value")
        node2 = Node(label="Node2Label", value="Node2Value")

        valid_vertex = Vertex(head=node1, tail=node2)
        invalid_vertex = Vertex(head=node2, tail=Node(label="Node3Label", value="Node3Value"))

        with self.assertRaises(Exception) as context:
            graph = Graph(nodes={node1, node2}, vertices=[valid_vertex, invalid_vertex])

        self.assertEqual(
            str(context.exception),
            "All vertices need to be only connected to nodes within the graph."
        )


if __name__ == '__main__':
    unittest.main()
