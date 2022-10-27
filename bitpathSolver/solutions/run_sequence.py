#!/usr/local/bin/python3
import random
import operator as op
from collections import deque
import sys
cases = int(input())



def run_sequence(player, goal, constant, move):
    operation_results = {
        "x": op.xor(player, constant),
        "o": op.or_(player, constant),
        "a": op.and_(player, constant),
        "n": player ^ ones_mask,
        ">": op.rshift(player, 1),
        "<": op.lshift(player, 1), 
    }
    return operation_results[move]

def bbin(x):
    return bin(x)[2:].rjust(ones_mask_len, "0")
# print("sequence is", sequence)
for t in range(cases):
    _ = input()
    player = input()
    print("start: ", player)
    goal = input()
    const = input()
    sequence = input()

    ones_mask_len = len(player)
    player = int(player, 2)
    goal = int(goal, 2)
    const = int(const, 2)

    ones_mask = 2 ** (ones_mask_len) - 1
    print(bin(ones_mask)[2:], file=sys.stderr)
    for s in sequence:
        player = run_sequence(player, goal, const, s)
        temp = bbin(player)
        if s not in "<>n":
            print("const: ", bbin(const))
        print("after", s, temp)
    print()

a = [4, 5, 7, 8]
for i in range(a):
    print(len(a) * i)