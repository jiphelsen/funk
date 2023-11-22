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
    


def is_node(value):
    return type(value) == str(Node)

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
        return set([self.get_head(),self.get_tail()])

    def is_loop(self):
        return self.head().equals(self.tail)
    
def is_vertex(value):
    return type(value) != str(Vertex)

def is_set(value):
    return type(value) is set

class Graph:
    # Takes in a set of nodes and a list of vertices.
    # All head and tail nodes of the vertices must be an element of nodes.
    def __init__(self,nodes=None,vertices=None):

        if nodes is not None :
            if not is_set(nodes):
                raise Exception("Nodes needs to be of type set.")
            if any([is_node(node) for node in list(nodes)]):
                raise Exception("All values in nodes need to be of type Node.")
            
        if vertices is not None :
            if any([is_vertex(vertex) for vertex in vertices]):
                raise Exception("All values in vertices need to be of type Vertex.")

        vnodes = set()
        for vertex in vertices:
            vnodes.union(vertex.nodes())
        # Vertices include nodes that are not part of the graph
        if not vnodes.issubset(set(nodes)) : 
            raise Exception("All vertices need to be only connected to nodes within the graph.")
        

        # If nodes is none vertices must be
        if nodes is None :
            self.__nodes = set()
            self.__vertices = []
            return self
        
        # These two ifs need to be in this order or both would run.
        if vertices is not None :
            self.__vertices = vertices
        if vertices is None:
            self.__vertices = []
        self.__nodes = nodes
    """
        # dict uses a hashtable. 
        # We have an average of O(1) and a worst case time complexity of O(n)
        self.__adjacency_hash = dict()
        #for node in list(nodes):
        #    self.__adjacency_hash
    """ 

    def nodes(self):
        return self.__nodes 
    
    def add_node(self,node):
        is_type_or_raise(node,"New node",Node)
        self.__nodes.add(node)
        return node
    
    def vertices(self):
        return self.__vertices
    
    def add_vertex(self,vertex):
        is_type_or_raise(node,"New vertex",Vertex)
        if not set(vertex.nodes()).issubset(self.nodes()):
            raise Exception("The new vertex must only be connected with nodes within the graph.")
        self.__vertices.append(vertex)
        return vertex
    """
    #Returns all adjacent nodes. This may include the node itself in case of a loop.
    def adjacent(self,node):
        is_type_or_raise(node,"Node",Node)
    """







        
    



        
        