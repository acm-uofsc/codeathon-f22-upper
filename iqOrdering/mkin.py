#!/usr/local/bin/python3
import random
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(2, 3)
    print(100, 100)
    print(99, 100, 101)
elif case_num == 1:
    print(3, 4)
    print(3, 6, 8)
    print(3, 7, 8, 9)
else:
    highest_possible_iq = 1_000_000_000
    number_of_history_people = random.randint(2, 10)
    num_visitors = random.randint(2, 10)
    extra = random.randint(0, 2)

    if case_num > 10:
        num_visitors = random.randint(90_000, 100_000)
        number_of_history_people = random.randint(100_000, 110_000)
    if case_num > 25:
        num_visitors = 200_000
        number_of_history_people = 500_000
        repeat = 10_000
        history_people = [random.randint(highest_possible_iq - 10, highest_possible_iq)
                          for i in range(number_of_history_people // repeat)]*repeat
        extra = 0
    else:
        history_people = [random.randint(highest_possible_iq - 10_000, highest_possible_iq)
                          for i in range(number_of_history_people)]
    history_people.sort()
    visitors = [random.choice(history_people) + extra
                for i in range(num_visitors)]

    print(number_of_history_people, num_visitors)
    print(*history_people)
    print(*visitors)
