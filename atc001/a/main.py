from collections import deque

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]

for y in range(H):
    for x in range(W):
        if C[y][x] == 's':
            sx, sy = x, y
        if C[y][x] == 'g':
            gx, gy = x, y

Q = deque()
Q.append((sx, sy))
ok = False
while len(Q) > 0:
    x, y = Q.pop()
    visited[y][x] = True
    for xx, yy in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if not (0 <= xx < W and 0 <= yy < H):
            continue
        if visited[yy][xx]:
            continue
        if C[yy][xx] == '#':
            continue
        if xx == gx and yy == gy:
            ok = True
            break
        Q.append((xx, yy))

print('Yes') if ok else print('No')
