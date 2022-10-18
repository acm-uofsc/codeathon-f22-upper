from collections import Counter

input()
input()
votes = input().split()

majority, _ = Counter(votes).most_common(1)[0]
print(majority)
