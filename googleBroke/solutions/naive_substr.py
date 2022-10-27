n, m = list(map(int, input().split()))

auto = [input() for _ in range(n)]

input()

typed = [input() for _ in range(m)]

for search in typed:
    count = 0
    for a in auto:
        for prefix_end in range(1, len(a) + 1):
            if search.startswith(a[:prefix_end]):
                count += 1
            else:
                break
    print(count)