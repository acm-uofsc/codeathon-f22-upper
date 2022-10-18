#!/usr/local/bin/python3
import random
from string import ascii_uppercase

MIN_CAND = 10
MAX_CAND = 25

NUM_VOTES = list(map(int, [1e6, 1e3, 1e2, 1e6, 1e6, 1e2, 1e2, 1e2, 1e2, 1e2]))


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
    num_candidates = random.randint(3, 15)
    total_votes = 20
    print(num_candidates, total_votes)

    candidates = [i for i in range(num_candidates)]
    print(*candidates)

    winner = random.choice(candidates)
    winner_margin = random.randint(
        total_votes // 2, total_votes // 2 + total_votes // 4)
    votes = [winner] * winner_margin
    votes += random.choices(candidates, k=(total_votes - winner_margin))
    random.shuffle(votes)
    print(*votes)
else:
    num_candidates = random.randint(MIN_CAND, MAX_CAND)
    total_votes = NUM_VOTES[case_num % len(NUM_VOTES)]
    print(num_candidates, total_votes)

    candidates = [i for i in range(num_candidates)]
    print(*candidates)

    winner = random.choice(candidates)
    winner_margin = random.randint(
        total_votes // 2, total_votes // 2 + total_votes // 4)
    votes = [winner] * winner_margin
    votes += random.choices(candidates, k=(total_votes - winner_margin))
    random.shuffle(votes)
    print(*votes)
