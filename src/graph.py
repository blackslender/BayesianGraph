from abc import ABC
from typing import Union, TypeVar


class Node(ABC):
    def __init__(self, node_name: str):
        # Prevent initialization of abstract class
        if type(self) is Node:
            raise Exception(
                "Node class is abstract, and cannot be used to create instances")
        self.__none_name = node_name

    def connect(self, target, weight=None):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. Any class that inherit the Node class must implement the connect method")
        return Edge(self, target, weight=weight)

    def name(self):
        return self.__node_name


class Edge():
    def __init__(self, source: Node, target: Node, weight=None):
        # raise NotImplementedError()  # TODO
        self.node_source, self.target, self.weight = source, target, weight

    def reverse(self):
        return Edge(self.target, self.source, weight=self.weight)


class UndirectedNode(Node):

    def __init__(self, nodename: str):
        super(UndirectedGraph, self).__init__(nodename)
        self.__edges = []

    def connect(self, target: Node, weight=None):
        edge = super(UndirectedNode, self).connect(target)
        self.__edges.append(edge)
        target.get_edges().append(edge.reverse())
        return edge

    def get_edges(self):
        return self.__edges

    def iter_neighbor_nodes(self):
        for edge in self.__edges:
            if self is edge.source:
                yield edge.target
            else:
                yield edge.source

    def iter_edges(self):
        for edge in self.__edges:
            yield edge


class DirectedNode(Node):
    def __init__(self, nodename: str):
        self.name = nodename
        self.__edges_in = []
        self.__edges_out = []

    def get_edges_in(self):
        return self.__edges_in

    def get_edges_out(self):
        return self.__edges_out

    def connect(self, target: Node, weight=None):
        # Connect current node to another node, and return the edge
        edge = super(DirectedNode, self).connect(target, weight=weight)
        self.__edges_out.append(edge)
        target.get_edges_in().append(edge)
        return edge

    def iter_out_nodes(self):
        ''' Iterate through the nodes which this node have an edge to'''
        for edge in self.get_edges_out():
            yield edge.target

    def iter_out_edges(self):
        for edge in self.get_edges_out():
            yield edge

    def iter_back_nodes(self):
        ''' Iterate through the nodes which have an edge connecting to this node '''
        for edge in self.get_edges_in():
            yield edge.source

    def iter_in_edges(self):
        for edge in self.get_edges_in():
            yield edge


class Graph(ABC):

    def __init__(self):

        # Prevent initialization of abstract class
        if type(self) is Graph:
            raise Exception(
                "Graph class is abstract, and cannot be used to create instances")
        self.__node_library = dict()
        self.__node_list
        self.__edge_list = []

    def insert_node(self, node: Node):
        # If node is string, create new node, otherwise add the node directly
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must implement the add_node method")
        self.__node_list.append(node)
        self.__node_library[node.name()] = node

    def connect(self, node_from: Node, node_to: Node, weight=None):
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must implement the connect method")
        edge = node_from.connect(node_to)
        self.__edge_list.append(edge)

    def traverse(self, func, function_args: tuple = (), mode='DFS' * args):
        '''
            This method provides a way to traverse through the graph
            The function will be called as function(node, *function_args)'''
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must implement the traverse method")
        if not callable(func):
            raise Exception(
                "'func' parameter must be a callable object (function)")

    def get_node(self, node_name: str):
        try:
            return self.__node_library[node_name]
        except KeyError as e:
            raise KeyError("The node name cannot be found in the graph")


class DirectedGraph(Graph):
    def __init__(self):
        super(DirectedGraph, self).__init__()

    def check_DAG(self):
        raise NotImplementedError()  # TODO

    def add_node(self, node: DirectedNode):
        super(DirectedGraph, self).add_node(node)
        # If node is string, create new node, otherwise add the node directly
        raise NotImplementedError()  # TODO

    def connect(self, node_from: DirectedNode, node_to: DirectedNode):
        super(DirectedGraph, self).connect(node_from, node_to)
        raise NotImplementedError()  # TODO

    def traverse(self, func, function_args: tuple = (), traverse_mode='DFS', start_at=None, *args):
        '''
            Traverse through the graph\n
            traverse_mode: can be "DFS" or "BFS"\n
            start_at: name of the required starting node; if none, the nodes which is insert earlier will have higher priority
        '''
        super(DirectedGraph, self).traverse(func, function_args, *args)
        if type(start_at) is str:
            start_at = Graph.
        # raise NotImplementedError()  # TODO

    def __dfs_traverse(self, func, function_args: tuple = (), start_at=None * args):
        traverse_result = dict()


class UndirectedGraph(Graph):

    def __init__(self):
        super(UndirectedGraph, self).__init__()
        raise NotImplementedError()  # TODO

    def add_node(self, node: UndirectedNode):
        super(UndirectedGraph, self).add_node(node)
        # If node is string, create new node, otherwise add the node directly
        raise NotImplementedError()  # TODO

    def connect(self, node_from: UndirectedNode, node_to: UndirectedNode):
        super(UndirectedGraph, self).connect(node_from, node_to)
        raise NotImplementedError()  # TODO

    def traverse(self, func, function_args: tuple = (), *args):
        super(UndirectedGraph, self).traverse(func, function_args, *args)
        raise NotImplementedError()  # TODO


# if __name__ == "__main__":
#     pass
