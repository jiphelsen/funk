class Node:
    def __init__(self,label=None,value=None):
        self.__value = value
        self.__label = label
    
    def set_value(self,value=None):
        self.__value = value
        return value
    
    def value(self):
        return self.__value
    
    def set_label(self,value=None):
        self.__label = value
        return value
    
    def label(self):
        return self.__label
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.label() == other.label() and self.value() == other.value()
        return False
    def __hash__(self):
        return hash((self.label(), self.value()))
    def __str__(self):
        return "(value="+str(self.value())+", label="+str(self.label())+")"


def is_node(value):
    return type(value) is Node

# params : value : value to check,s : name of the value, t : type of the value
def is_type_or_raise(value, s, t):
    if value is None:
        raise Exception(f"{s} can not be None.")
    if type(value) != t:
        raise Exception(f"{s} needs to be of type {t}.")
    return None

class Vertex:
    def __init__(self, head,tail):
        is_type_or_raise(head,"Head",Node)
        is_type_or_raise(tail,"Tail",Node)
        self.__head = head
        self.__tail = tail

    def head(self):
        return self.__head
    
    def tail(self):
        return self.__tail
    
    def set_head(self,node):
        is_type_or_raise(node,"New head",Node)
        self.__head = node
        return node
    
    def set_tail(self,node):
        is_type_or_raise(node,"New tail",Node)
        self.__tail = node
        return node
    
    # Returns a set of the head an the tail
    def nodes(self):
        return set([self.head(),self.tail()])

    def is_loop(self):
        return self.head() == self.tail()
    
def is_vertex(value):
    return type(value) is Vertex

def is_set(value):
    return type(value) is set

class Graph:
    # Takes in a set of nodes and a list of vertices.
    # All head and tail nodes of the vertices must be an element of nodes.
    def __init__(self,nodes=None,vertices=None):

        if nodes is not None :
            if not is_set(nodes):
                raise Exception("Nodes needs to be of type set.")
            if any([not is_node(node) for node in list(nodes)]):
                raise Exception("All values in nodes need to be of type Node.")
            
        if vertices is not None :
            if any([not is_vertex(vertex) for vertex in vertices]):
                raise Exception("All values in vertices need to be of type Vertex.")

            vnodes = set()
            for vertex in vertices:
                vnodes = vnodes.union(vertex.nodes())
            
            # Vertices include nodes that are not part of the graph
            if not vnodes.issubset(set(nodes)) : 
                raise Exception("All vertices need to be only connected to nodes within the graph.")
        

        # If nodes is none vertices must be
        if nodes is None :
            self.__nodes = set()
            self.__vertices = []
            return
        
        # These two ifs need to be in this order or both would run.
        if vertices is not None :
            self.__vertices = vertices
        if vertices is None:
            self.__vertices = []
        self.__nodes = nodes

        # Dictionary to store the adjacency hash node -> adjacend nodes 
        self.__adjacency_hash = {node: set() for node in self.__nodes}

        # Update de adjacency_hash op basis van vertices
        for vertex in self.__vertices:
            head, tail = vertex.head(), vertex.tail()
            self.__adjacency_hash[head].add(tail)
            self.__adjacency_hash[tail].add(head)

    def nodes(self):
        return self.__nodes 
    
    def add_node(self,node):
        is_type_or_raise(node,"New node",Node)
        self.__nodes.add(node)
        return node
    
    def vertices(self):
        return self.__vertices
    
    def add_vertex(self,vertex):
        is_type_or_raise(vertex,"New vertex",Vertex)
        if not set(vertex.nodes()).issubset(self.nodes()):
            raise Exception("The new vertex must only be connected with nodes within the graph.")
        self.__vertices.append(vertex)
        return vertex
    
    def adjacency(self, node):
        is_type_or_raise(node, "Node", Node)
        return self.__adjacency_hash[node]

    






        
    



        
        