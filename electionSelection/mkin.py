#!/usr/local/bin/python3
import random
from string import ascii_uppercase

MIN_CAND = 10
MAX_CAND = 1000

NUM_VOTES= list(map(int, [1e6,1e2,1e2,1e6,1e6,1e2,1e2,1e2,1e2,1e2]))

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
    num_candidates = 2
    total_votes = 10
    print(num_candidates, total_votes)

    candidates = [i for i in range(num_candidates)]
    print(*candidates)

    votes = []
    for i in range(num_candidates):
        if i == 0:
            votes += [candidates[i]] * (total_votes // 2 + 1)
        else:
            votes.append(candidates[i])
    if len(votes) != total_votes:
        votes += [candidates[-1]] * (total_votes - len(votes))

    random.shuffle(votes)
    print(*votes)
elif case_num == 1:
    num_candidates = 5
    total_votes = 10
    print(num_candidates, total_votes)

    candidates = [i for i in range(num_candidates)]
    print(*candidates)
    votes = []
    for i in range(len(candidates)):
        votes.append(candidates[i])
        votes.append(candidates[i])
    random.shuffle(votes)
    print(*votes)
else:
    num_candidates = random.randint(MIN_CAND, MAX_CAND)
    total_votes = NUM_VOTES[case_num % len(NUM_VOTES)]
    print(num_candidates, total_votes)

    candidates = [i for i in range(num_candidates)]
    print(*candidates)
    vote_weights = [total_votes // num_candidates + 1] + [(total_votes - (total_votes // num_candidates + 1)) //
                                                          (num_candidates - 1)] * (num_candidates - 1)
    votes = random.choices(candidates, weights=vote_weights, k=total_votes)
    random.shuffle(votes)
    print(*votes)

