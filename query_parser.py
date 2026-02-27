from tokenizer import clean

# take a string clean it and return it in a list of word/words
def query_parser(query_string):
    
    # initiate empty list
    word_list = []
    
    # split the string into a list of words
    split_query = query_string.split()
    
    # loop through that list and clean the words
    for word in split_query:
        clean_word = clean(word)
        
        # if "cleaned word" is an empty string continue 
        if clean_word == "":
            continue
        
        # if not append cleaned word to list
        else:
            word_list.append(clean_word)
    
    # return list
    return word_list