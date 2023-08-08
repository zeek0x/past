from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

diff = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        d = 0
        for k in range(M):
            if S[i][k] != S[j][k]:
                d += 1
        diff[i][j] = diff[j][i] = d

G = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        G[i][j] = diff[i][j] == 1

def isReachable(path):
    prev = path[0]
    for i in range(1, N):
        if not G[prev][path[i]]:
            return False
        prev = path[i]
    return True

ok = False
for path in permutations(range(N)):
    if isReachable(path):
        ok = True
        break

print('Yes') if ok else print('No')
