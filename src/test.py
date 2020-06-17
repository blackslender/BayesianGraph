from DAG import DAG
import unittest

class TestDAGMethods(unittest.TestCase):

    def test_traverse(self):
        dag = DAG()
        nodelist = list(dag.traverse(lambda x: x))
        self.assertEqual(len(nodelist), 0)     

    def test_add_node(self):
        dag = DAG()
        dag.add_node("A")
        dag.add_node("B")
        nodelist = list(dag.traverse(lambda x: x.name))
        self.assertEqual(nodelist, ["A","B"])    

    def test_add_node_exception(self):
        try:
            dag = DAG()
            dag.add_node("A")
            dag.add_node("A")
        except Exception as e:
            self.assertEqual(str(e), "Duplicate node in one graph.")

    def test_connect_edge(self):
        dag = DAG()
        dag.add_node("A")
        dag.add_node("B")
        dag.connect("A", "B")
        nodelist = list(dag.traverse(lambda x: x.get_edge_str()))
        self.assertEqual(nodelist, [["A -> B"],[]])

if __name__ == '__main__':
    unittest.main()