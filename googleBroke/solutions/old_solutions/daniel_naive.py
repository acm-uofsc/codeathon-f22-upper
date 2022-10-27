n, m = list(map(int, input().split()))

auto = [input() for _ in range(n)]

input()

typed = [input() for _ in range(m)]

for search in typed:
    count = 0
    for a in auto:
        if search.startswith(a):
            count += 1
    print(count)