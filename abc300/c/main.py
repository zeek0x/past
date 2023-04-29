H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
N = min(H, W)

cross = [0] * (N+1)


def is_cross(i, j, n):
    return (i+n < H and j+n < W and C[i+n][j+n] == '#') and \
        (i+n < H and j-n >= 0 and C[i+n][j-n] == '#') and \
        (i-n >= 0 and j-n >= 0 and C[i-n][j-n] == '#') and \
        (i-n >= 0 and j+n < W and C[i-n][j+n] == '#')


for i in range(H):
    for j in range(W):
        if C[i][j] != '#':
            continue

        for n in range(N):
            if is_cross(i, j, n+1):
                continue
            else:
                cross[n] += 1
                break

print(*cross[1:])
