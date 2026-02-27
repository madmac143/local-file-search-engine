from query_parser import query_parser
from search_engine import search
from rank import rank_results

def run_search(index, query_string):
    
    # clean and tokenize the user query
    word_list = query_parser(query_string)
    
    # if user typed nothing stop and return empty list
    if word_list == []:
        return []
    
    # run AND-search against inverted index
    matching_files = search(index, word_list)
    
    # if no files contain all the tokens stop and return empty list
    if matching_files == []:
        return []
    
    # score and sort the matching files by revelance greatest to least
    ranked_files = rank_results(index, matching_files, word_list)

    # return results
    return ranked_files