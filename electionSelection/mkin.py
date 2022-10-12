#!/usr/local/bin/python3
import random
from string import ascii_uppercase

MIN_CAND = 2
MAX_CAND = 100

MIN_VOTES = 10000
MAX_VOTES - 1e7


def gen_candidate():
    letter = random.choice(ascii_uppercase)
    numbers = random.choices(range(9), k=8)
    numbers.insert(0, letter)
    return ''.join(map(str, numbers))


def gen_candidates(n_candidates):
    candidates = []
    while len(candidates) < n_candidates:
        candidate = gen_candidate()
        if candidate not in candidates:
            candidates.append(candidate)
    return candidates


case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    num_candidates = 3
    total_votes = 10
    print(num_candidates, total_votes)

    candidates = gen_candidates(num_candidates)
    print(*candidates)
    vote_weights = [total_votes // num_candidates + 1] + [(total_votes - (total_votes // num_candidates + 1)) //
                                                          (num_candidates - 1)] * (num_candidates - 1)
    votes = random.choices(candidates, weights=vote_weights, k=total_votes)
    random.shuffle(votes)
    print(*votes)
elif case_num == 1:
    print(5, 4)
else:
    # output what should be read in as input by
    # contestant code
    n = random.randint(3, 100000)
    j = random.randint(3, 2 ** 25)
    print(n, j)
