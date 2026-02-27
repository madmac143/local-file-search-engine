def search(index, query_tokens):
    
    # if query tokens(user input) is empty return empty list
    if not query_tokens:
        return []
    
    # assign variable to first query token if does not exist return empty list 
    first_token = query_tokens[0]
    if first_token not in index:
        return []
    
    # create a set of all files that contain first word in query
    result_set = set(index[first_token].keys())

    # loop through the rest of the query tokens (words user input)
    for token in query_tokens[1:]:
        if token not in index:
            return []
       
        # create a set of all files that contain this word
        token_files = set(index[token].keys())

        # create a set of the result of only files that contain every word so far
        result_set = result_set.intersection(token_files)

        # if nothing is left then no file contains all the words
        if not result_set:
            return []

    #return the final list of files that matched every word in the form of a list
    return list(result_set)
            