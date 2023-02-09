N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1 << N
INF = 10**100
cost = [[INF]*N for _ in range(ALL)]
cost[0][0] = 0


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(
                cost[n | (1 << j)][j], cost[n][i] + A[i][j]
            )

print(cost[ALL-1][0])
