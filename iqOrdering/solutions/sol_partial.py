import bisect
num_history_people, num_visitors = list(
    map(int, input().split()))
history_people = list(map(int, input().split()))
assert len(history_people) == num_history_people 

visitors = [int(x) for x in input().split()]
for visitor in visitors:
    smarter_than = bisect.bisect_left(history_people, visitor)
    # smarter_or_equal_to = bisect.bisect_right(history_people, visitor)
    smarter_or_equal_to = smarter_than
    for i in range(smarter_than, num_history_people):
        if history_people[i] == visitor:
            smarter_or_equal_to += 1
        else:
            break
    print(smarter_than, smarter_or_equal_to)
