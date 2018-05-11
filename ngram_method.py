import os
import sys
import math
import glob
import helper_functions as helpers

# Make dictionaries of counts of unigrams and bigrams
helpers.train_classifier("data/moviereviews/neg/*", "neg")
helpers.train_classifier("data/moviereviews/pos/*", "pos")

correct = 0.0
incorrect = 0.0
for filename in glob.glob("data/moviereviews/neg/*"):
    valence = helpers.classify(filename)
    if valence == "Negative":
        correct += 1.0
    else:
        incorrect += 1.0
print("Performance on negative reviews: ", correct/(correct+incorrect))

correct = 0.0
incorrect = 0.0
for filename in glob.glob("data/moviereviews/pos/*"):
    valence = helpers.classify(filename)
    if valence == "Positive":
        correct += 1.0
    else:
        incorrect += 1.0
print("Performance on positive reviews: ", correct/(correct+incorrect))
