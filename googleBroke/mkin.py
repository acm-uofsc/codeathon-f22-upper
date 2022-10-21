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
        n = random.randint(180, 200) * 5
        prefix_len = random.randint(4500, 5000)
        m = 2000
    print(n, m)
    # prefix_len = random.randint(3, 20 if case_num < easy_cases_cutoff else 5000)
    prefix = "".join(random.choices(string.ascii_letters, k=prefix_len-min(10, prefix_len-2)))
    suffix_len = 5
    after = random.sample(string.ascii_letters, k=suffix_len)
    auto_completes = []
    for i in range(n//5):
        for j in range(suffix_len):
            auto_completes.append(prefix+(after[j]*(i+1)))
    random.shuffle(auto_completes)
    assert len(set(auto_completes)) == n
    for q in auto_completes:
        print(q)
    print(FILLER_LINE)
    searches = []
    for x in range(m):
        searches.append(random.choice(auto_completes) +
                        random.choice(string.ascii_letters))
    for x in searches:
        print(x)

