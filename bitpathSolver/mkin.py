#!/usr/local/bin/python3
import random
import operator as op
from collections import deque
import sys
case_num = int(input())
random.seed(case_num)


# 0 and 1 are the sample cases
if case_num == 0:
    print("2")
    print(">")
    print("1000")
    print("0010")
    print("0000")
    print("<>")
    print("111110000")
    print("000001100")
    print("000000000")
elif case_num == 1:
    print("1")
    print("<a")
    print("1111111")
    print("0110000")
    print("0111110")
elif case_num == 2:
    print("1")
    print(">nox")
    print("00000001010")
    print("11100100100")
    print("11001000101")
else:
    def get_ops(player, constant):
        operation_results = [
            (op.xor(player, constant), "x"),
            (op.or_(player, constant), "o"),
            (op.and_(player, constant), "a"),
            (player ^ ones_mask, "n"),
            (op.rshift(player, 1), f"> by {1}"),
            (op.lshift(player, 1), f"< by {1}")
        ]
        if case_num < 20:
            if case_num % 2== 0:
                operation_results = operation_results[:len(operation_results)//2]
            else:
                operation_results = operation_results[len(operation_results)//2:]
        else:
            if case_num % 2 == 0:
                operation_results.pop(0)
            if case_num % 5 == 0:
                operation_results.pop(1)
            if case_num % 3 == 0:
                operation_results.pop(1)
        in_constraints = [res for res in operation_results
                          if res[0] < ones_mask]
        return in_constraints

    def bfs(const, start, limit):
        fringe = deque([(start, "")])
        seen = {}
        while fringe:
            cur, steps = fringe.popleft()
            # print("fringe len", len(fringe), file=sys.stderr)
            if len(steps) >= limit:
                break
            if len(seen) > 20000:
                break
            if cur in seen:
                continue
            seen[cur] = steps
            options = get_ops(cur, const)
            random.shuffle(options)
            for result, symbol in options:
                letter = symbol[0]
                fringe.append((result, steps + letter))
        return seen

    # output what should be read in as input by
    # contestant code
    CASES = random.randint(5, 15)
    # CASES = 10
    print(CASES)
    for t in range(CASES):
        ones_mask = 2 ** (random.randint(min(20, case_num + 3), 28)) - 1
        start = random.randint(ones_mask // 2, ones_mask)
        ones_mask_len = len(bin(ones_mask)[2:])
        start_bin = bin(start)[2:].rjust(ones_mask_len, "0")
        const = random.randint(0, ones_mask)
        const_bin = bin(const)[2:].rjust(ones_mask_len, "0")
        state_to_moves = bfs(const, start, max(5, case_num // 2))
        options = [option for option in state_to_moves.keys()
                   if len(state_to_moves[option]) >= 1]
        # options.sort(key=lambda x: (
        #     (len(state_to_moves[x]))
        # ))
        # if case_num > 20:
            # end_state = options[-1]
            # options = options[len(options)//2:]
        # else:
        end_state = random.choice(options)
        end_state_bin = bin(end_state)[2:].rjust(ones_mask_len, "0")
        symbols_used = state_to_moves[end_state]
        print("".join(set(symbols_used)))
        print(start_bin)
        print(end_state_bin)
        print(const_bin)
        # print("ones mask\n", bin(ones_mask)[2:])
        # print("answer was", symbols_used, file=sys.stderr)
