import nltk
import glob

def clean_text(the_text):
    tokens = nltk.word_tokenize(the_text)
    return tokens

def get_bigrams(the_text):
    bigrams = nltk.bigrams(the_text)
    return bigrams

neg_bigrams = {}
neg_unigrams = {}
neg_wdct = 0
pos_bigrams = {}
pos_unigrams = {}
pos_wdct = 0
def train_classifier(path, valence):
    global neg_bigrams
    global neg_unigrams
    global neg_wdct
    global pos_bigrams
    global pos_unigrams
    global pos_wdct

    for filename in glob.glob(path):
        f = open(filename)
        review = f.read()
        tokens = clean_text(review)
        grams = get_bigrams(tokens)

        if valence == "neg":
            for token in tokens:
                neg_wdct += 1
                if token in neg_unigrams.keys():
                    neg_unigrams[token] += 1
                else:
                    neg_unigrams[token] = 1

            for gram in grams:
                if gram in neg_bigrams.keys():
                    neg_bigrams[gram] += 1
                else:
                    neg_bigrams[gram] = 1
        else:
            for token in tokens:
                pos_wdct += 1
                if token in pos_unigrams.keys():
                    pos_unigrams[token] += 1
                else:
                    pos_unigrams[token] = 1

            for gram in grams:
                if gram in pos_bigrams.keys():
                    pos_bigrams[gram] += 1
                else:
                    pos_bigrams[gram] = 1

        f.close()
