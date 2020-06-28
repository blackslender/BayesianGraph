
import numpy as np

from graph import DirectedNode, DirectedGraph


def get_segment_idx(segments, number):
    low = 0
    for i in range(len(segments)):
        if number >= low and number < low+segments[i]:
            return i
        else:
            low += segments[i]
    return i


class BayesNode(DirectedNode):
    def __init__(self, nodename, parent_names, node_values, prob_table):
        super(BayesNode, self).__init__(nodename)
        self._parent_names = parent_names
        self._node_values = node_values
        self._prob_table = prob_table

    def get_value_at_index(self, index):
        return self._node_values[index]

    def get_parent_names(self):
        return self._parent_names

    def get_prob_table(self):
        return self._prob_table


class BayesGraph(DirectedGraph):
    def __init__(self):
        super(BayesGraph, self).__init__()

    def forward_generator(self, sample_number):
        node_number = len(self._nodes)
        self.__sample_data = []
        for _ in range(sample_number):
            continous_sample = np.random.rand(node_number)
            discrete_sample = []
            discrete_idx = {}
            for node, f in zip(self._nodes, continous_sample):
                if len(node.get_parent_names()) > 0:
                    parent_value_idxes = [discrete_idx[name]
                                          for name in node.get_parent_names()]
                    distribution = node.get_prob_table()[
                        tuple(parent_value_idxes)]
                else:
                    distribution = node.get_prob_table()
                value_idx = get_segment_idx(distribution, f)
                value = node.get_value_at_index(value_idx)
                discrete_sample.append(value)
                discrete_idx[node.name()] = value_idx
            self.__sample_data.append(discrete_sample)
        print("Length samples: ", len(self.__sample_data))
        # print("SAMPLES:", self.__sample_data)

    def build_filter(self, conditions):
        node_names = [node.name() for node in self._nodes]
        conds = []
        for k,v in conditions.items():
            idx = node_names.index(k)
            # conds.append(lambda x: x[idx]==v)
            conds.append((idx, v))
        return conds

    def query(self, query):
        variables = query[0]
        conditions = query[1]
        conds = self.build_filter(conditions)
        # import pdb; pdb.set_trace()
        satisfy = list(filter(lambda x: all([x[k]==v for k,v in conds]), self.__sample_data))
        # print("Length satisfy: ", len(satisfy))
        var_conds = self.build_filter(variables)
        res = list(filter(lambda x: all([x[k]==v for k,v in var_conds]), satisfy))
        # print("Length results: ", len(res))
        return round(len(res)/len(satisfy), 7)
        # print("RESULTS:", res)
        
                

