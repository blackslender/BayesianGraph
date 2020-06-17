from abc import ABC
from typing import Union, TypeVar


class Node(ABC):
    def __init__(self, nodename: str):

        # Prevent initialization of abstract class
        if type(self) is Node:
            raise Exception(
                "Node class is abstract, and cannot be used to create instances")

        # raise NotImplementedError()  # TODO

    def connect(self, target):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. Any class that inherit the Node class must implement the connect method")
        return Edge(self, target)


class UndirectedNode(Node):

    def __init__(self, nodename: str):
        self.name = nodename
        # raise NotImplementedError()  # TODO

    def connect(self, target: Union[str, Node]):
        super(UndirectedNode, self).connect(target)
        raise NotImplementedError()  # TODO


class DirectedNode(Node):
    def __init__(self, nodename: str):
        self.name = nodename
        # raise NotImplementedError()  # TODO

    def connect(self, target: Union[str, Node]):
        # Connect current node to another node, and return the edge
        super(DirectedNode, self).connect(target)
        raise NotImplementedError()  # TODO


class Edge():
    def __init__(self, node_from: Union[str, Node], node_to: Union[str, Node], weight=None):
        raise NotImplementedError()  # TODO


class Graph(ABC):

    def __init__(self):

        # Prevent initialization of abstract class
        if type(self) is Graph:
            raise Exception(
                "Graph class is abstract, and cannot be used to create instances")
        self.__nodelist = []
        self.__edgelist = []

    def add_node(self, node: Union[str, Node]):
        # If node is string, create new node, otherwise add the node directly
        raise NotImplementedError(
            "This method is not implemented in the current class. Any class that inherit the Graph class must implement the add_node method")

    def connect(self, node_from: Union[str, Node], node_to: Union[str, Node]):
        raise NotImplementedError(
            "This method is not implemented in the current class. Any class that inherit the Graph class must implement the connect method")

    def traverse(self, func, function_args: tuple = (), *args):
        '''
            This method provides a way to traverse through the graph
            The function will be called as function(node, *function_args)'''
        if not callable(func):
            raise Exception(
                "func parameter must be a callable object (function)")

        raise NotImplementedError(
            "This method is not implemented in the current class. Any class that inherit the Graph class must implement the traverse method")


class DirectedGraph(Graph):
    def __init__(self):
        super(DirectedGraph, self).__init__()

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


# if __name__ == "__main__":
#     pass