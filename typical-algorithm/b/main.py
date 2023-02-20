N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda ab: ab[1])

ans = 0
prev_end = 0
for ab in AB:
    if prev_end < ab[0]:
        ans += 1
        prev_end = ab[1]

print(ans)
