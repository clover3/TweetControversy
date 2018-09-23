
from collections import Counter

class OddScore:
    def __init__(self):
        f = open("oddscores.txt", "r", encoding="utf-8")
        self.odd_dict = Counter()
        for line in f:
            tokens = line.split()
            word = tokens[0]
            score = float(tokens[1])
            self.odd_dict[word] = score

    def predict(self, doc):
        tokens = doc.split(" ")
        odd_sum = 0
        for token in tokens:
            odd_sum += self.odd_dict[token.lower()]
        return odd_sum

