from bayesian import BayesGraph, BayesNode
import numpy as np
<<<<<<< HEAD


=======
>>>>>>> origin/dag
class Parser():
    def __init__(self):
        pass

    @staticmethod
    def parse_node_info(line):
        comps = line.split(';')
        nodename = comps[0]
<<<<<<< HEAD
        parent_nodes = comps[1].split(',') if len(comps[1]) > 0 else []
        node_values = comps[2].split(',')
        table_shape = tuple([int(ele) for ele in comps[3].split(',')])
        prob_table = np.array(comps[4].split(',')).reshape(
            table_shape).astype(np.float32)
=======
        parent_nodes = comps[1].split(',') if len(comps[1])>0 else []
        node_values = comps[2].split(',')
        table_shape = tuple([int(ele) for ele in comps[3].split(',')])
        prob_table = np.array(comps[4].split(',')).reshape(table_shape).astype(np.float32)
>>>>>>> origin/dag
        return nodename, parent_nodes, node_values, prob_table

    @staticmethod
    def parse_query_info(line):
        comps = line.split(';')
        variables = comps[0].split(',')
<<<<<<< HEAD
        variables = [{item.split('=')[0]:item.split('=')[1]}
                     for item in variables]
        conditions = comps[1].split(',') if len(comps[1]) > 0 else []
        conditions = [{item.split('=')[0]:item.split('=')[1]}
                      for item in conditions]
        print(variables, conditions)
        return variables, conditions


class ModelBuilder():
    def __init__(self):
        pass

=======
        variables = [{item.split('=')[0]:item.split('=')[1]} for item in variables]
        conditions = comps[1].split(',') if len(comps[1])>0 else [] 
        conditions = [{item.split('=')[0]:item.split('=')[1]} for item in conditions]
        print(variables, conditions)
        return variables, conditions

class ModelBuilder():
    def __init__(self):
        pass
    
>>>>>>> origin/dag
    @staticmethod
    def build_model_from_file(model, model_file):
        with open(model_file, 'r') as inp:
            lines = inp.read().split('\n')
<<<<<<< HEAD
            # check line number
            # if int(lines[0]) != len(lines) - 1:
            #     raise Exception("Mismatch at line number")
            for line in lines[1:]:
                nodename, parent_nodes, node_values, prob_table = Parser.parse_node_info(
                    line)
                new_node = BayesNode(nodename, parent_nodes,
                                     node_values, prob_table)
=======
            #check line number
            # if int(lines[0]) != len(lines) - 1:
            #     raise Exception("Mismatch at line number")
            for line in lines[1:]:
                nodename, parent_nodes, node_values, prob_table = Parser.parse_node_info(line)
                new_node = BayesNode(nodename, parent_nodes, node_values, prob_table)
>>>>>>> origin/dag
                model.add_node(new_node)
                for parent in parent_nodes:
                    model.connect(parent, nodename)
        print([x.name() for x in model._nodes])
        return model

<<<<<<< HEAD

=======
>>>>>>> origin/dag
class QueryBuilder():
    def __init__(self):
        self.queries = []

    def build_query_from_file(self, query_file):
        with open(query_file, 'r') as inp:
            lines = inp.read().split('\n')
<<<<<<< HEAD
            # check line number
=======
            #check line number
>>>>>>> origin/dag
            # if int(lines[0]) != len(lines) - 1:
            #     raise Exception("Mismatch at line number")
            for line in lines[1:]:
                variables, conditions = Parser.parse_query_info(line)
                self.queries.append((variables, conditions))
<<<<<<< HEAD
=======

>>>>>>> origin/dag
