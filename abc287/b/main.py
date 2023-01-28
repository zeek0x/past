N, M = map(int, input().split())
S = [input() for _ in range(N)]
M = [input() for _ in range(M)]

ans = 0
for s in S:
    for m in M:
        if s[-3:] == m:
            ans += 1
            break

print(ans)
