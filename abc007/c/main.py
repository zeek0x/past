from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(R)]
dist = [[-1 for _ in range(C)]for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

Q = deque()
Q.append((sx, sy))
dist[sy][sx] = 0
while len(Q) > 0:
    x, y = Q.popleft()
    for xx, yy in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if xx > C - 1 or xx < 0 or yy > R - 1 or yy < 0:
            continue
        if maze[yy][xx] != '.':
            continue
        if dist[yy][xx] != -1:
            continue

        dist[yy][xx] = dist[y][x] + 1

        if xx == gx and yy == gy:
            break

        Q.append((xx, yy))

print(dist[gy][gx])
