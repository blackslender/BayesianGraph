import sys
from builder import ModelBuilder, QueryBuilder, FileOperator
from bayesian import BayesGraph
def main(argv):
    import time
    start = time.time()
    model_path, query_path = argv[2], argv[4]
    #Build model
    bayes_model = ModelBuilder.build_model_from_file(BayesGraph(), model_path)
    bayes_model.forward_generator(sample_number=10**6)
    #Build query
    query_obj = QueryBuilder()
    query_obj.build_query_from_file(query_path)  
    queries = query_obj.get_queries()
    #Inference
    res = [bayes_model.query(q) for q in queries]
    #Export output
    output_path = "outputs/"+model_path.split('/')[1]+'/output.txt'
    FileOperator.write_to_file(output_path, res)
    print("Time:", time.time()-start)
if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)
    