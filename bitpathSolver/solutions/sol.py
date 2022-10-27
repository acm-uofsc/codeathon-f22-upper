from collections import deque
import operator as op
import sys

def get_ops(player, constant):
    operation_results = [
        (op.xor(player, constant), "x"),
        (op.or_(player, constant), "o"),
        (op.and_(player, constant), "a"),
        (op.inv(player) & ones_mask, "n"),
        (op.rshift(player, 1), f"> by {1}"),
        (op.lshift(player, 1), f"< by {1}")
    ]

    in_constraints = [res for res in operation_results
                      if res[0] < ones_mask and
                      res[1][0] in allowed_this_time]
    return in_constraints


def bfs(goal, const, start):
    fringe = deque([(start, "")])
    seen = set()
    while fringe:
        cur, steps = fringe.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        if cur == goal:
            return (cur, steps)
        for result, symbol in get_ops(cur, const):
            letter = symbol[0]
            fringe.append((result, steps + letter))

    assert False, "no answer found"


possible = "xoan<>"
CASES = int(input())
for i in range(CASES):
    allowed_this_time = set(input())
    assert all(x in possible for x in allowed_this_time), allowed_this_time
    editing_row = input()
    goal_row = input()
    const_row = input()
    row_len = len(editing_row)
    assert len(editing_row) == len(goal_row) == len(const_row)

    editing_row = int(editing_row, 2)
    goal_row = int(goal_row, 2)
    const_row = int(const_row, 2)
    ones_mask = 2 ** (row_len) - 1

    answer = bfs(goal_row, const_row, editing_row)
    print(len(answer[1]))
    print(answer[1], file=sys.stderr)
