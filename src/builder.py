from bayesian import BayesGraph, BayesNode
import numpy as np
import os

class FileOperator():
    def __init__(self):
        pass

    @staticmethod
    def parse_node_info(line):
        comps = line.split(';')
        nodename = comps[0]
        parent_nodes = comps[1].split(',') if len(comps[1]) > 0 else []
        node_values = comps[2].split(',')
        table_shape = tuple([int(ele) for ele in comps[3].split(',')])
        prob_table = np.array(comps[4].split(',')).reshape(
            table_shape).astype(np.float32)
        return nodename, parent_nodes, node_values, prob_table

    @staticmethod
    def parse_query_info(line):
        comps = line.split(';')
        variables = comps[0].split(',')
        var_dict, condition_dict = {},{}
        for item in variables:
            k, v = item.split('=')
            var_dict[k] = v
        conditions = comps[1].split(',') if len(comps[1])>0 else [] 
        for item in conditions:
            k, v = item.split('=')
            condition_dict[k] = v
        print("Query: ", var_dict, condition_dict)
        return var_dict, condition_dict

    @staticmethod
    def write_to_file(file_path, content):
        try:
            os.mkdir(file_path[:-10]) # cut output.txt
        except Exception as e:
            print(e)
        with open(file_path, "w+") as f:
            f.write("\n".join([str(c) for c in content]))

class ModelBuilder():
    def __init__(self):
        pass

    @staticmethod
    def build_model_from_file(model, model_file):
        with open(model_file, 'r') as inp:
            lines = inp.read().split('\n')
            # check line number
            # if int(lines[0]) != len(lines) - 1:
            #     raise Exception("Mismatch at line number")
            for line in lines[1:]:
                nodename, parent_nodes, node_values, prob_table = FileOperator.parse_node_info(
                    line)
                new_node = BayesNode(nodename, parent_nodes,
                                     node_values, prob_table)
                model.add_node(new_node)
                for parent in parent_nodes:
                    model.connect(parent, nodename)
        print("Node list: ", [x.name() for x in model._nodes])
        return model

class QueryBuilder():
    def __init__(self):
        self.__queries = []

    def build_query_from_file(self, query_file):
        with open(query_file, 'r') as inp:
            lines = inp.read().split('\n')
            # check line number
            # if int(lines[0]) != len(lines) - 1:
            #     raise Exception("Mismatch at line number")
            for line in lines[1:]:
                variables, conditions = FileOperator.parse_query_info(line)
                self.__queries.append((variables, conditions))

    def get_queries(self):
        return self.__queries