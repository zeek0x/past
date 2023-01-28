from collections import deque

N, M = map(int, input().split())
U, V = [], []
for _ in range(M):
    u, v = map(int, input().split())
    U.append(u-1)
    V.append(v-1)

E = [[] for _ in range(N)]
visited = [False]*N

for i in range(M):
    E[U[i]].append(V[i])
    E[V[i]].append(U[i])

ok = True
Q = deque()
Q.append((0, -1,))
while len(Q) > 0:
    i, prev = Q.pop()

    if visited[i]:
        ok = False
        break

    visited[i] = True

    for j in E[i]:
        if j != prev:
            Q.append((j, i))

ok = ok and all(visited)

print('Yes') if ok else print('No')
