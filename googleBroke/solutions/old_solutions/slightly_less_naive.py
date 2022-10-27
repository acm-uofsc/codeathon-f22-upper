
n, m = map(int, input().split())
auto_completes = [input() for _ in range(n)]
_ = input()
to_type = [input() for _ in range(m)]
# auto_completes.sort()
for i_type in to_type:
    count = 0
    for auto in auto_completes:
        if i_type.startswith(auto):
            count += 1

    print(count)
