import nltk
import glob
import math

stopwords = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"]

def clean_text(the_text):
    global stopwords
    tokens = nltk.word_tokenize(the_text)
    meaningful_tokens = []
    for token in tokens:
        if token not in stopwords:
            meaningful_tokens.append(token)
    return meaningful_tokens

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

def classify(filename):
    neg_score = 0
    pos_score = 0

    f = open(filename)
    review = f.read()
    tokens = clean_text(review)
    grams = get_bigrams(tokens)

    for gram in grams:
        if gram in neg_bigrams.keys():
            neg_score += math.log(neg_bigrams[gram])/math.log(neg_wdct)
        if gram in pos_bigrams.keys():
            pos_score += math.log(pos_bigrams[gram])/math.log(pos_wdct)
        else:
            word = gram[1]
            if word in neg_unigrams.keys():
                neg_score += neg_unigrams[word]/(neg_wdct)
            if word in pos_unigrams.keys():
                pos_score += pos_unigrams[word]/(pos_wdct)

#    pos_score /= pos_wdct
#    neg_score /= neg_wdct
#    print(pos_score, "\t", neg_score)
    if pos_score > neg_score:
        return("Positive")
    else:
        return("Negative")
