from abc import ABC
from typing import Union, TypeVar


class Node(ABC):
    __node_library = dict()

    def __init__(self, node_name=None):

        # Prevent initialization of abstract class
        if type(self) is Node:
            raise Exception(
                "Node class is abstract, and cannot be used to create instances")
        if node_name is None:
            node_name = 'NODE_' + str(len(self._node_library))
        self.__name = node_name

        if self in self._node_library:
            raise Exception(
                "Node name is used. For a single runtime, a unique name only belongs to a single node.")
        self._node_library[node_name] = self

    def connect(self, target: Union[str, Node], weight=None):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the connect method")
        if type(target) is str:
            try:
                target = self._node_library[target]
            except KeyError as _:
                raise KeyError("Trying to connect to an unknown node name")
        return Edge(self, target, weight=weight)

    @staticmethod
    def static_connect(node_from: Union[str, Node], node_to: Union[str, Node], weight=None):
        return node_from.connect(node_to, weight=weight)

    @staticmethod
    def get_global_node_by_name(node_name):
        try:
            node = __node_library[node_name]
            return node
        except


class UndirectedNode(Node):

    def __init__(self, node_name=None):
        super(UndirectedNode, self).__init__(node_name)
        self.__edges = set()

    def connect(self, target: Union[str, UndirectedNode], weight=None):
        edge = super(UndirectedNode, self).connect(target, weight=weight)
        self.__edges.add(edge)
        return edge

    def edge_iter(self):
        for edge in self.__edges:
            yield edge
        raise StopIteration()


class DirectedNode(Node):
    def __init__(self, node_name=None):
        super(DirectedNode, self).__init__(node_name)

        # raise NotImplementedError()  # TODO
        self.__in_edges = set()
        self.__out_edges = set()

    def connect(self, target: Union[str, DirectedNode], weight=None):
        # Connect current node to another node, and return the edge
        edge = super(DirectedNode, self).connect(target)

        # Key exception is already handled in the parent class
        if type(target) is str:
            target = super._node_library[target]
        self.__out_edges.add(edge)
        target.__in_edges.add(edge)
        return edge

    def in_edge_iter(self):
        for edge in self.__in_edges:
            yield edge
        raise StopIteration()

    def out_edge_iter(self):
        for edge in self.__out_edges:
            yield edge
        raise StopIteration()


class Edge:
    def __init__(self, node_from: Union[str, Node], node_to: Union[str, Node], weight=None):
        self.__node_from = node_from
        self.__node_to = node_to
        self.__weight = weight

    def source(self):
        return self.__node_from

    def target(self):
        return self.__node_to


class Graph(ABC):

    def __init__(self):

        # Prevent initialization of abstract class
        if type(self) is Graph:
            raise Exception(
                "Graph class is abstract, and cannot be used to create instances")
        self.__node_list = []
        self.__edge_list = []

    def add_node(self, node: Union[str, Node]):
        # If node is string, create new node, otherwise add the node directly
        if type(node) is str:
            try:
                node = Node._node_library[node]
            except KeyError as _:

        raise NotImplementedError(
            "This method is not implemented in the current class. "
            "Any class that inherit the Graph class must implement the add_node method")

    def connect(self, node_from: Union[str, Node], node_to: Union[str, Node]):
        raise NotImplementedError(
            "This method is not implemented in the current class. "
            "Any class that inherit the Graph class must implement the connect method")

    def traverse(self, func, function_args: tuple = (), *args):
        '''
            This method provides a way to traverse through the graph
            The function will be called as function(node, *function_args)'''
        if not callable(func):
            raise Exception(
                "func parameter must be a callable object (function)")

        raise NotImplementedError(
            "This method is not implemented in the current class. "
            "Any class that inherit the Graph class must implement the traverse method")


class DirectedGraph(Graph):
    def __init__(self):
        super(DirectedGraph, self).__init__()

        raise NotImplementedError()  # TODO

    def check_DAG(self):
        raise NotImplementedError()  # TODO

    def add_node(self, node: Union[str, DirectedNode]):
        super(DirectedGraph, self).add_node(node)
        # If node is string, create new node, otherwise add the node directly
        raise NotImplementedError()  # TODO

    def connect(self, node_from: Union[str, DirectedNode], node_to: Union[str, DirectedNode]):
        super(DirectedGraph, self).connect(node_from, node_to)
        raise NotImplementedError()  # TODO

    def traverse(self, func, function_args: tuple = (), *args):
        super(DirectedGraph, self).traverse(func, function_args, *args)
        raise NotImplementedError()  # TODO


class UndirectedGraph(Graph):

    def __init__(self):
        super(UndirectedGraph, self).__init__()
        raise NotImplementedError()  # TODO

    def add_node(self, node: Union[str, UndirectedNode]):
        super(UndirectedGraph, self).add_node(node)
        # If node is string, create new node, otherwise add the node directly
        raise NotImplementedError()  # TODO

    def connect(self, node_from: Union[str, UndirectedNode], node_to: Union[str, UndirectedNode]):
        super(UndirectedGraph, self).connect(node_from, node_to)
        raise NotImplementedError()  # TODO

    def traverse(self, func, function_args: tuple = (), *args):
        super(UndirectedGraph, self).traverse(func, function_args, *args)
        raise NotImplementedError()  # TODO


if __name__ == "__main__":
    pass
