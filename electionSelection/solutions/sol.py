input()
input()
votes = input().split()

# Boyer Moore Majority Vote Algorithm
majority = -1
i = 0
for j in range(len(votes)):
    if i == 0:
        majority = votes[j]
        i = 1
    elif majority == votes[j]:
        i = i + 1
    else:
        i = i - 1

print(majority)
