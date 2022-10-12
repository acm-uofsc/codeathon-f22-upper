from collections import Counter
import timeit

input()
input()

votes = input().split()


def main():
    majority = Counter(votes).most_common(1)[0]
    # print(majority[0])


print(timeit.timeit(main, number=10000))
