from graph import *
import numpy as np

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
    def forward_generator(self, sample_number):
        node_number = len(self._nodes)
        self._sample_data = []
        for _ in range(sample_number): 
            continous_sample = np.random.rand(node_number)
            discrete_sample = []
            discrete_idx = {}
            for node, f in zip(self._nodes, continous_sample):
                if len(node.get_parent_names()) > 0:
                    parent_value_idxes = [discrete_idx[name] for name in node.get_parent_names()] 
                    distribution = node.get_prob_table()[tuple(parent_value_idxes)]
                else:
                    distribution = node.get_prob_table()
                value_idx = get_segment_idx(distribution, f)
                value = node.get_value_at_index(value_idx)
                discrete_sample.append(value)
                discrete_idx[node.name()] = value_idx
            self._sample_data.append(discrete_sample)
        print(self._sample_data)
        
                

