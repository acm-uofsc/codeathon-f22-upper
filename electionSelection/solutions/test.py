from collections import Counter

input()
input()
votes = input().split()


majority, n_votes = Counter(votes).most_common(1)[0]

if n_votes < (len(votes) // 2 + 1):
    print('None')
else:
    print(majority)
