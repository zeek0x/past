import math

N, M = map(int, input().split())
INF = 10**16
ans = INF
for a in range(1, int(math.sqrt(M)) + 1):
    b = math.ceil(M / a)
    if a <= N and b <= N:
        ans = min(ans, a * b)

print(ans) if ans != INF else print(-1)
