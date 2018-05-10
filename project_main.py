import os
import glob
import math
import helper_functions as helpers

path = "data/moviereviews/neg/*"
neg_counts = {}
neg_total = 0

for filename in glob.glob(path):
    f = open(filename)
    review = f.read()

    words = helpers.clean_text(review)
    for word in words:
        if word not in neg_counts.keys():
            neg_counts[word] = 1
        else:
            neg_counts[word] += 1
    neg_total += 1

    f.close()

#pruned_neg = {}
#for key in neg_counts.keys():
#    if neg_counts[key] >= 3:
#        pruned_neg[key] = neg_counts[key]

path = "data/moviereviews/pos/*"
pos_counts = {}
pos_total = 0

for filename in glob.glob(path):
    f = open(filename)
    review = f.read()

    words = helpers.clean_text(review)
    for word in words:
        if word not in pos_counts.keys():
            pos_counts[word] = 1
        else:
            pos_counts[word] += 1
    pos_total += 1

    f.close()

#pruned_pos = {}
#for key in pos_counts.keys():
#    if pos_counts[key] >= 3:
#        pruned_pos[key] = pos_counts[key]
predic_neg = 0
predic_pos = 0
print("Analyzing negative reviews...")
path = "data/moviereviews/neg/*"
for filename in glob.glob(path):
    neg_score = 0
    pos_score = 0
    f = open(filename)
    review = f.read()

    words = helpers.clean_text(review)
    for word in words:
        if word in neg_counts:
            neg_score += neg_counts[word]
        if word in pos_counts:
            pos_score += pos_counts[word]
    if pos_score > neg_score*1.15:
        predic_pos += 1
    else:
        predic_neg +=1
#    print("pos: ", pos_score, ", neg: ", neg_score*1.2)

    f.close()
print("Accuracy on negative reviews: ", predic_neg/neg_total)

predic_neg = 0
predic_pos = 0
print("Analyzing positive reviews...")
path = "data/moviereviews/pos/*"
for filename in glob.glob(path):
    neg_score = 0
    pos_score = 0
    f = open(filename)
    review = f.read()

    words = helpers.clean_text(review)
    for word in words:
        if word in neg_counts:
            neg_score +=neg_counts[word]
        if word in pos_counts:
            pos_score += pos_counts[word]
    if pos_score > neg_score*1.15:
        predic_pos += 1
    else:
        predic_neg +=1
#    print("pos: ", pos_score, ", neg: ", neg_score*1.15)

    f.close()
print("Accuracy on positive reviews: ", predic_pos/pos_total)
