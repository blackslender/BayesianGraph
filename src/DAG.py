# Review: This class seems not to be necessary. The DirectedGraph class has already implemented these features


from graph import *
from typing import Union, TypeVar
import numpy as np


class DAGNode(DirectedNode):
    def __init__(self, nodename: str):
        super(DAGNode, self).__init__(nodename)
        # self.__next = []      # This is implement

    def connect(self, target: Union[str, DirectedNode]):
        # Connect current node to another node, and return the edge
        self.__next.append(target)

    def get_next_vertices(self):
        return self.__next

    def get_edge_str(self):
        return ["{} -> {}".format(self.name, x.name) for x in self.__next]


class DAG(DirectedGraph):
    def __init__(self):
        super(DAG, self).__init__()
        self.__nodelist = []
        self.__edgelist = []

    def get_node_by_name(self, name):
        for v in self.__nodelist:
            if v.name == name:
                return v
        return None

    def sort_topo(self):
        #num_nodes = len(self.__nodelist)
        #edge_matrix = np.zeros((num_nodes, num_nodes))
        #vectice_index = {}
        # for i,node in enumerate(self.__nodelist):
        #    vectice_index[node.name] = i

    def check_DAG(self):
        raise NotImplementedError()  # TODO

    def add_node(self, node: Union[str, DirectedNode]):
        temp = self.get_node_by_name(node)
        if temp is not None:
            raise Exception("Duplicate node in one graph.")
        else:
            self.__nodelist.append(DAGNode(node))

    def connect(self, node_from: Union[str, DirectedNode], node_to: Union[str, DirectedNode]):
        source = self.get_node_by_name(node_from)
        target = self.get_node_by_name(node_to)
        if source is not None and target is not None:
            source.connect(target)
        else:
            raise Exception("Source or target is not in this graph.")

    def traverse(self, func, function_args: tuple = (), *args):
        return map(lambda x: func(x, *function_args), self.__nodelist)
