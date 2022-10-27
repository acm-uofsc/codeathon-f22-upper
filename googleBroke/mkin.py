#!/usr/local/bin/python3
import random
import string
case_num = int(input())
random.seed(case_num)
FILLER_LINE = "I typed this:"
# 0 and 1 are the sample cases
if case_num == 0:
    print(3, 1)
    print("car")
    print("carb")
    print("carbos")
    print("I typed this:")
    print("carbuncle")
elif case_num == 1:
    print(5, 3)
    print("three")
    print("tree")
    print("fort")
    print("trees")
    print("t")
    print(FILLER_LINE)
    print("tree")
    print("t")
    print("iAmForteeTree")
else:
    # output what should be read in as input by
    # contestant code
    easy_cases_cutoff = 15
    if case_num < 5:
        n = 10
        m = 10
        prefix_len = random.randint(3, 6)
    elif case_num < easy_cases_cutoff:
        n = random.randint(4, 50) * 5
        m = random.randint(4, 50) * 10
        prefix_len = random.randint(3, 20)
    else:
        n = random.randint(100, 120) * 5
        prefix_len = random.randint(3000, 3200)
        m = 1000
    print(n, m)
    # prefix_len = random.randint(3, 20 if case_num < easy_cases_cutoff else 5000)
    prefix = "".join(random.choices(string.ascii_letters, k=prefix_len-min(10, prefix_len-2)))
    # if case_num < easy_cases_cutoff:
    #     suffix_len = 
    # else:
    suffix_len = n
    # after = random.sample(string.ascii_letters, k=suffix_len)
    suffix = "".join(random.choices(string.ascii_letters, k=suffix_len))
    auto_completes = []
    # assert n % suffix_len == 0
    for i in range(n):
        auto_completes.append(prefix + suffix[:i])
    last = auto_completes[-1]
    random.shuffle(auto_completes)
    assert len(set(auto_completes)) == n
    for q in auto_completes:
        print(q)
    print(FILLER_LINE)
    searches = []
    end2 = "".join(random.choices(string.ascii_letters, k=m))
    for x in range(m):
        if case_num > easy_cases_cutoff:
            chosen = last
        else:
            chosen = random.choice(auto_completes)
        # extra = "".join(random.choices(string.ascii_letters, k=(x // 100) + 3))
        off = random.randint(1, 100)
        if off > 95:
            temp = list(chosen)
            temp[random.randint(0, len(temp) - 1)] = random.choice(string.ascii_letters)
            temp = "".join(temp)
            searches.append(temp + end2[:x] + random.choice(string.ascii_letters))
        else:
            searches.append(chosen + end2[:x] + random.choice(string.ascii_letters))
    random.shuffle(searches)
    for x in searches:
        print(x)

