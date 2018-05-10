import os
import math
import helper_functions as helpers

# Make dictionaries of counts of unigrams and bigrams
helpers.train_classifier("data/moviereviews/neg/*", "neg")
helpers.train_classifier("data/moviereviews/pos/*", "pos")
