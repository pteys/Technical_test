class SparseArray:
    def __init__(self,strings,queries):
        self.strings = strings
        self.queries = queries
        self.n = len(strings)
        self.q = len(queries)
        
    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')

    #Self as an initialized SparseArray
        #For each query in self.queries[]
        #Count the number of occurrences in self.strings[]
        #Returns q_results{}: count of occurrences of queries[] in strings[]
    def matching_strings(self):
        q_results = {}      
        for query in self.queries:
            q_results[query] = self.strings.count(query)
        return q_results
    
