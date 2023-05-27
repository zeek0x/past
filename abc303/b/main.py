N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

E = [set() for _ in range(N)]

for i in range(M):
    for j in range(N - 1):
        x = A[i][j] - 1
        y = A[i][j + 1] - 1
        E[x].add(y)
        E[y].add(x)

ans = 0

for i in range(N):
    ans += N - len(E[i]) - 1

print(ans//2)
