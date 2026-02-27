import re

# helper function
# takes a word and makes it lower case and takes any numbers or characters out of it
def clean(word):
    
    word = word.lower()
    word = re.sub(r"[^a-z]+", "", word)
    return word 

# main function
# splits the text into words and cleans them and returns them in list
def tokenize(text):
    
    # initaite empty list and create word variable by splitting text
    word_list = []
    words = text.split()

    # loops through all words in list and cleans them and appends them to list
    for raw_word in words:
        clean_word = clean(raw_word)
        
        # if the "cleaned word" is an empty string continue
        if clean_word == "":
            continue
        
        # appends word to list
        word_list.append(clean_word)
    
    # returns list
    return word_list