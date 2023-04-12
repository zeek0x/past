N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

n = 0
visited = [False] * N


def dfs(i):
    visited[i] = True
    for j in G[i]:
        if visited[j]:
            continue
        dfs(j)


for i in range(N):
    if visited[i]:
        continue
    n += 1
    dfs(i)

print(n)
