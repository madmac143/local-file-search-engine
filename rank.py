def rank_results(index, files, query_tokens):
    
    # set up a score for each file we already know matched the search
    scores = {}
    for file in files:
        scores[file] = 0

    # go through each word the user searched for
    for token in query_tokens:
        
        # grab the file: count mapping for this word for the inverted index
        token_info = index[token]
        
        # check each file and add the count if this word is in it
        for file in files:
            if file in token_info:
                
                # add however many times the word shows up to its score
                scores[file] += token_info[file]

    # sort the files by the score (highest score = most relevant) then return them 
    sorted_scores = sorted(files, key=lambda f: scores[f], reverse=True)
    return sorted_scores