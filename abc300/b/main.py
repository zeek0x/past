H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]


def solve():
    for i in range(H):
        for j in range(W):
            ok = True
            for y in range(H):
                for x in range(W):
                    if A[(y+i) % H][(x+j) % W] != B[y][x]:
                        ok = False
                        break
            if ok:
                return True
    return False


print('Yes') if solve() else print('No')
