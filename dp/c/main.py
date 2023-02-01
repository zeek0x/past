N = int(input())
ABC = [()]
for _ in range(N):
    ABC.append(tuple(map(int, input().split())))

dp = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + ABC[i][1], dp[i-1][2] + ABC[i][2])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + ABC[i][0], dp[i-1][2] + ABC[i][2])
    dp[i][2] = max(dp[i-1][2], dp[i-1][1] + ABC[i][1], dp[i-1][0] + ABC[i][0])

print(max(dp[N]))
