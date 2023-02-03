N, M = map(int, input().split())
A = list(map(list, [input() for _ in range(N)]))

group = [[] for _ in range(11)]
for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            n = 0
        elif A[i][j] == 'G':
            n = 10
        else:
            n = int(A[i][j])
        group[n].append((i, j))

cost = []
INF = 2 << 60
for i in range(N):
    cost.append([INF]*M)

si, sj = group[0][0]
cost[si][sj] = 0

for n in range(1, 11):
    for i, j in group[n]:
        for ii, jj in group[n-1]:
            cost[i][j] = min(cost[i][j], cost[ii][jj] + abs(i-ii) + abs(j-jj))

gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == INF:
    ans = -1

print(ans)
