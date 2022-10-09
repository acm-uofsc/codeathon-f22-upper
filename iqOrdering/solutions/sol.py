import bisect
num_history_people, num_visitors = list(
    map(int, input().split()))
history_people = list(map(int, input().split()))
assert len(history_people) == num_history_people 

visitors = [int(x) for x in input().split()]
for visitor in visitors:
    smarter_than = bisect.bisect_left(history_people, visitor)
    smarter_or_equal_to = bisect.bisect_right(history_people, visitor)
    print(smarter_than, smarter_or_equal_to)