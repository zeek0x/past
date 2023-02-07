from collections import deque

N, M = map(int, input().split())
G = [list() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

visited = [False] * N
S = 0
for i in range(N):
    if not visited[i]:
        S += 1
        Q = deque()
        Q.append(i)
        while len(Q) > 0:
            v = Q.pop()
            for j in G[v]:
                if not visited[j]:
                    visited[j] = True
                    Q.append(j)
print(M - N + S)
