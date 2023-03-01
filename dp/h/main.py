H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

cnt = [[0]*W for _ in range(H)]

MOD = 10**9 + 7

cnt[0][0] = 1
for y in range(1, H):
    if A[y][0] == '.':
        cnt[y][0] = cnt[y-1][0]
for x in range(1, W):
    if A[0][x] == '.':
        cnt[0][x] = cnt[0][x-1]
for y in range(1, H):
    for x in range(1, W):
        if A[y][x] == '.':
            cnt[y][x] = (cnt[y-1][x] + cnt[y][x-1]) % MOD

print(cnt[H-1][W-1])
