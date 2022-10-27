from functools import reduce
from sys import stderr
import json
from collections import defaultdict as dd
TrieNode = lambda : dd(TrieNode)
trie = TrieNode()
n, m = map(int, input().split())
auto_completes = [input() for _ in range(n)]
_ = input()
to_type = [input() for _ in range(m)]

END = "#"
COUNT = 'count'
for word in auto_completes:
    cur_node = trie
    #fancy way to add each word to the trie
    # reduce(dict.__getitem__, word, trie)[END] = True
    for letter in word:
        cur_node = cur_node[letter]
        if COUNT not in cur_node:
            cur_node[COUNT] = 1
        else:
            cur_node[COUNT] += 1

    # cur_node[END] = True


for query in to_type:
    cur = trie
    count = 0
    for letter in query:
        cur = cur[letter]
        if COUNT in cur:
            count += cur[COUNT]
    print(count)

