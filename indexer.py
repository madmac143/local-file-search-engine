from tokenizer import tokenize 
from extractor import extract_text

# build an inverted index using tokenize function
def build_index(file_index):
    
    # initiate empty dictionary 
    invert_index = {}
    
    # loop through index
    for record in file_index:
        path = record["path"]

        # extract text from file
        text = extract_text(path)
        
        # use tokenize function to create clean word list
        word_list = tokenize(text)
        
        # loop through word list
        for word in word_list:
            
            # if the cleaned word is not in the index, add it
            if word not in invert_index:
                invert_index[word] = {}
            
            # if this file has not been seen for this word, initialize count
            if path not in invert_index[word]:
                invert_index[word][path] = 0

            # increment the count for this word in this file
            invert_index[word][path] += 1
    
    # return index
    return invert_index
