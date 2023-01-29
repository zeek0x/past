N, X = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[False for _ in range(X+1)] for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        for k in range(B[i]+1):
            if j >= A[i]*k:
                if dp[i][j-A[i]*k]:
                    dp[i+1][j] = True

print('Yes') if dp[N][X] else print('No')
