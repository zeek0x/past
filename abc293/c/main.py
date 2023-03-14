import sys
sys.setrecursionlimit(10*100)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

cnt = 0


def dfs(x, y, s: set):
    a = A[y][x]
    if a in s:
        return

    if x + 1 == W and y + 1 == H:
        global cnt
        cnt += 1
        return

    sc = s.copy()
    sc.add(a)

    if x + 1 < W:
        dfs(x+1, y, sc)
    if y + 1 < H:
        dfs(x, y+1, sc)


dfs(0, 0, set())

print(cnt)
