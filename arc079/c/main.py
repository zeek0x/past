from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1 for _ in range(N)]
Q = deque()
Q.append(0)
dist[0] = 0
while len(Q) > 0:
    i = Q.popleft()

    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

print("POSSIBLE") if dist[N-1] == 2 else print("IMPOSSIBLE")
