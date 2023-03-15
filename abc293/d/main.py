from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
D = [0] * N

for _ in range(M):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    G[a].append(c)
    G[c].append(a)
    D[a] += 1
    D[c] += 1

used = [False] * N

X, Y = 0, 0
for i in range(N):
    if used[i]:
        continue
    used[i] = True

    Q = deque()
    Q.append(i)
    cycle = True
    while len(Q) > 0:
        j = Q.pop()
        if D[j] != 2:
            cycle = False
        for k in G[j]:
            if used[k]:
                continue
            Q.append(k)
            used[k] = True
    if cycle:
        X += 1
    else:
        Y += 1

print('{} {}'.format(X, Y))
