from SparseArray import SparseArray
import os
import argparse

def main():
    #Parse a list of query as argument
    parser = argparse.ArgumentParser(description='Process a list of strings,\
                                                  count its occurrences inside the\
                                                  SPARSE_ARRAY_STRINGS environment variable,\
                                                  return a dictionary of the result')
    parser.add_argument('queries', metavar='query', type=str, nargs='+',
                        help='<required> Queries')
    
    args = parser.parse_args()
    queries = args.queries[0].split(',')

    #Get the SPARSE_ARRAY_STRINGS environment variable as a list of strings
    strings = os.environ.get('SPARSE_ARRAY_STRINGS').split(',')

    #Apply the matching_string() function of class SparseArray
    #to the list of query and the list of strings    
    with SparseArray(strings,queries) as sparse_array:
        print(sparse_array.matching_strings())


if __name__ == "__main__":
    main()
