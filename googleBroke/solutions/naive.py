
n, m = map(int, input().split())
auto_completes = [input() for _ in range(n)]
_ = input()
to_type = [input() for _ in range(m)]

for i_type in to_type:
    count = 0
    for end_point in range(1, len(i_type) + 1):
        for auto in auto_completes:
            if auto == i_type[:end_point]:
                count += 1
    print(count)
