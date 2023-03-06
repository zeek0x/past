from collections import deque


N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

S = int(input())
S -= 1
K = int(input())
T = list(map(lambda x: int(x) - 1, input().split()))

T.append(S)

Dist = []

INF = 10**1000
for t1 in T:
    dist = [INF] * N
    Q = deque()
    Q.append(t1)
    dist[t1] = 0
    while len(Q) > 0:
        i = Q.popleft()
        for j in edges[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                Q.append(j)
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

ALL = 1 << K
cost = [[INF]*K for _ in range(ALL)]

for i in range(K):
    cost[1 << i][i] = Dist[K][i]


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(
                cost[n | (1 << j)][j], cost[n][i] + Dist[i][j])

print(min(cost[ALL-1]))
