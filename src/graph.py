from abc import ABC
from typing import Union, TypeVar
from collections import OrderedDict, deque


class Edge:
    def __init__(self, source, target, weight=None):
        self.source, self.target, self.weight = source, target, weight

    def reverse(self):
        return Edge(self.target, self.source, weight=self.weight)


class Node(ABC):
    def __init__(self, node_name: str):
        # Prevent initialization of abstract class
        if type(self) is Node:
            raise Exception(
                "Node class is abstract, and cannot be used to create instances")
        self.__node_name = node_name
        self._edges = []

    def connect(self, target, weight=None):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the connect method")
        edge = Edge(self, target, weight=weight)
        self._append_edge(edge)
        target._append_edge(edge)
        return edge

    def _append_edge(self, edge: Edge):
        assert (edge.source is self) or (edge.target is self)
        self._edges.append(edge)

    def name(self):
        return self.__node_name

    def iter_out_edges(self):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the iter_out_edges method")

    def iter_in_edges(self):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the iter_in_edges method")

    def iter_out_nodes(self):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the iter_out_nodes method")

    def iter_in_nodes(self):
        if type(self) is Node:
            raise NotImplementedError(
                "This method is not implemented in current class. "
                "Any class that inherit the Node class must implement the iter_in_nodes method")


class UndirectedNode(Node):

    def __init__(self, nodename: str):
        super(UndirectedNode, self).__init__(nodename)

    def connect(self, target: Node, weight=None):
        """
        Create a new edge to connect between current node and target node
        """
        edge = super(UndirectedNode, self).connect(target, weight=weight)
        return edge

    def iter_out_nodes(self):
        for edge in self._edges:
            if edge.source is self:
                yield edge.target
            else:
                yield edge.source

    def iter_in_nodes(self):
        for edge in self._edges:
            if edge.source is self:
                yield edge.target
            else:
                yield edge.source

    def iter_in_edges(self):
        for edge in self._edges:
            if edge.source is self:
                yield edge.reverse()
            else:
                yield edge

    def iter_out_edges(self):
        for edge in self._edges:
            if edge.source is self:
                yield edge
            else:
                yield edge.reverse()


class DirectedNode(Node):
    def __init__(self, nodename: str):
        super(DirectedNode, self).__init__(nodename)

    def connect(self, target, weight=None):
        # Connect current node to another node, and return the edge
        edge = super(DirectedNode, self).connect(target, weight=weight)
        target._append_edge(edge)
        return edge

    def _append_edge(self, edge: Edge):
        assert (edge.source is self) or (edge.target is self)
        self._edges.append(edge)

    def iter_out_edges(self):
        for edge in self._edges:
            if edge.source is self:
                yield edge

    def iter_out_nodes(self):
        """ Iterate through the nodes which this node has an edge to"""
        for edge in self.iter_out_edges():
            yield edge.target

    def iter_in_edges(self):
        for edge in self._edges:
            if edge.target is self:
                yield edge

    def iter_in_nodes(self):
        """ Iterate through the nodes which have an edge connecting to this node """
        for edge in self.iter_in_edges():
            yield edge.source


class Graph(ABC):

    def __init__(self):

        # Prevent initialization of abstract class
        if type(self) is Graph:
            raise Exception(
                "Graph class is abstract, and cannot be used to create instances")
        self.__node_library = dict()  # node_name to Node dictionary
        self.__node_list = []
        self.__edge_list = []

    def add_node(self, node: Node):
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must "
                "implement the add_node method")
        self.__node_list.append(node)
        self.__node_library[node.name()] = node
        return node

    def connect(self, source, target, weight=None):
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must implement the connect method")
        if type(source) is str:
            source = self.get_node(source)
        if type(target) is str:
            target = self.get_node(target)
        edge = source.connect(target)
        self.__edge_list.append(edge)

    def traverse(self, func, func_args: tuple = (), *args):
        '''
            This method apply a function over nodes in the graph in DFS order\n
            The function will be called as func(node, *func_args)'''
        if type(self) is Graph:
            raise NotImplementedError(
                "This method is not implemented in the current class. Any class that inherit the Graph class must "
                "implement the traverse method")
        if not callable(func):
            raise Exception(
                "'func' parameter must be a callable object (function)")
        traverse_results = OrderedDict()  # Node name to result mapping
        visited_node = set()
        for node in self.__node_list:
            if node not in visited_node:
                traverse_stack = deque([node])
                while len(traverse_stack) != 0:
                    current_node = traverse_stack.pop()
                    traverse_results[current_node.name()] = func(
                        current_node, *func_args)
                    temp_stack = deque()
                    for next_node in current_node.iter_out_nodes():
                        temp_stack.append(next_node)
                    while len(temp_stack) > 0:
                        next_node = temp_stack.pop()
                        if next_node not in visited_node:
                            traverse_stack.append(temp_stack.pop())
                    visited_node.add(current_node)
        return traverse_results

    def get_node(self, node_name: str):
        try:
            return self.__node_library[node_name]
        except KeyError:
            raise KeyError("The node name cannot be found in the graph")


class DirectedGraph(Graph):
    def __init__(self):
        super(DirectedGraph, self).__init__()

    def check_DAG(self):
        raise NotImplementedError()  # TODO

    def topo_sort(self):
        # Re-order the node list to follow TOPO order
        raise NotImplementedError()  # TODO

    def add_node(self, node: DirectedNode):
        return super(DirectedGraph, self).add_node(node)

    def connect(self, source: DirectedNode, target: DirectedNode):
        return super(DirectedGraph, self).connect(source, target)

    def traverse(self, func, function_args: tuple = (), traverse_mode='DFS', start_at=None, *args):
        return super(DirectedGraph, self).traverse(func, function_args, *args)


class UndirectedGraph(Graph):

    def __init__(self):
        super(UndirectedGraph, self).__init__()

    def add_node(self, node: UndirectedNode):
        super(UndirectedGraph, self).add_node(node)

    def connect(self, source: UndirectedNode, target: UndirectedNode):
        return super(UndirectedGraph, self).connect(source, target)

    def traverse(self, func, function_args: tuple = (), *args):
        return super(UndirectedGraph, self).traverse(func, function_args, *args)


if __name__ == "__main__":
    a = DirectedGraph()
    node1 = DirectedNode("Node1")
    node2 = DirectedNode("Node2")
    a.add_node(node1)
    a.add_node(node2)
    a.connect(node2, node1)

    print(a.traverse(lambda x: x.name()))
