N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

MOD = 998244353

dp = [[0] * 2 for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, N):
    if A[i] != A[i-1]:
        dp[i][0] += (dp[i-1][0] % MOD)
    if A[i] != B[i-1]:
        dp[i][0] += (dp[i-1][1] % MOD)
    if B[i] != A[i-1]:
        dp[i][1] += (dp[i-1][0] % MOD)
    if B[i] != B[i-1]:
        dp[i][1] += (dp[i-1][1] % MOD)

print((dp[N-1][0]+dp[N-1][1]) % MOD)
