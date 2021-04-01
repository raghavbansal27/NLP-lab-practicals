from nltk.corpus import reuters
import nltk
nltk.download('reuters')
# reuters contains above 10 thousand news documents and million words
from nltk import bigrams, trigrams
from collections import defaultdict

model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurrence
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1

# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count


print(dict(model["the", "price"]))