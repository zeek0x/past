import sys

sys.setrecursionlimit(1_000_000_000)

T = int(input())

NDK = []
for _ in range(T):
    N, D, K = map(int, input().split())
    NDK.append((N, D, K))

_NDK = sorted(NDK, reverse=True, key=lambda ndk: ndk[2])

memo = {}


def solve(grid, mark, A, N, D, K):
    if N in memo:
        if D in memo[N]:
            if K in memo[N][D]:
                return memo[N][D][K]

    grid[A] = True
    mark += 1
    if mark >= K:
        if N not in memo:
            memo[N] = {}
        if D not in memo[N]:
            memo[N][D] = {}
        memo[N][D][K] = A
        return A

    x = (A+D) % N
    while grid[x]:
        x = (x+1) % N
    ret = solve(grid, mark, x, N, D, K)
    if N not in memo:
        memo[N] = {}
    if D not in memo[N]:
        memo[N][D] = {}
    memo[N][D][K] = ret
    return ret


for ndk in _NDK:
    n, d, k = ndk
    grid = [False] * n
    solve(grid, 0, 0, n, d, k)

for ndk in NDK:
    n, d, k = ndk
    print(memo[n][d][k])
