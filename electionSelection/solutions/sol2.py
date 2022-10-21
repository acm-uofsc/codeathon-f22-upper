from collections import Counter

n_elections = int(input().split()[-1])
input()

for _ in range(n_elections):
    votes = input().split()

    majority, _ = Counter(votes).most_common(1)[0]
    print(majority)
