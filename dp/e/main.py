N, W = map(int, input().split())
ws, vs = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

INF = 1 << 32
VMAX = 10 ** 5

dp = [[INF] * (VMAX + 1) for _ in range(N + 1)]
dp[0][0] = 0

for n in range(1, N+1):
    for v in range(VMAX + 1):
        dp[n][v] = dp[n-1][v]
        if v - vs[n] >= 0:
            dp[n][v] = min(dp[n][v], dp[n-1][v - vs[n]] + ws[n])

for v in range(VMAX + 1):
    if dp[N][v] <= W:
        ans = v

print(ans)
