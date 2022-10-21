
n, m = map(int, input().split())
auto_completes = [input() for _ in range(n)]
_ = input()
to_type = [input() for _ in range(m)]
auto_completes.sort()
for i_type in to_type:
    count = 0
    has_found_start = False
    for auto in auto_completes:
        if i_type.startswith(auto):
            has_found_start = True
            count += 1
        elif has_found_start:

    print(count)
