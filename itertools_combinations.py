"""
You are given a list of lowercase English letters.
For a given integer , you can select any indices
(assume 1-based indexing) with a uniform probability
from the list.
Find the probability that at least one of the indices
selected will contain the letter: ''.
"""
import itertools as it

SEARCH_CHAR = 'a'

N = int(input().strip())
SAMPLE = map(str, input().strip().split())
K = int(input())

combinations = list(it.combinations(SAMPLE, K))
total_combinations = len(combinations)
counter = it.count(0)
counter = [next(counter) for data in list(combinations) if SEARCH_CHAR in data]
print('Probability:', round(len(counter)/total_combinations, 3))
