import sys
sys.setrecursionlimit(10**9)

N = int(input())
R = -1
edges = [[] for _ in range(N)]

for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

Q = int(input())
queries = [[] for _ in range(N)]
for q in range(Q):
    a, b = map(int, input().split())
    queries[a-1].append([q, b-1])

ans = [False]*Q
boss = [False]*N

def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]
    boss[i] = True
    for j in edges[i]:
        dfs(j)
    boss[i] = False

dfs(R)

[print('Yes') if ans[q] else print('No') for q in range(Q)]
