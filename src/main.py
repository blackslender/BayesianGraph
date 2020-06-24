import sys
from builder import ModelBuilder, QueryBuilder
from bayesian import BayesGraph
def main(argv):
    model_file = argv[2]
    bayes_model = ModelBuilder.build_model_from_file(BayesGraph(), model_file)
    bayes_model.forward_generator(sample_number=10)
    query_file = argv[4]
    query_obj = QueryBuilder().build_query_from_file(query_file)  

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)
    