h, x = [int(x) for x in input().split()]
history = [int(x) for x in input().split()]
visitors = [int(x) for x in input().split()]

for visitor in visitors:
    greater_than = 0
    equal_or_greater = 0
    for i in range(len(history)):
        if visitor > history[i]:
            greater_than += 1
        if visitor >= history[i]:
            equal_or_greater += 1
        else:
            break
    print(greater_than, equal_or_greater)
