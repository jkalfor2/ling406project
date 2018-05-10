import nltk

def clean_text(the_text):
    tokens = nltk.word_tokenize(the_text)
    return tokens
