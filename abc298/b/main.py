N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def match(AA, BB):
    for i in range(N):
        for j in range(N):
            if BB[i][j] - AA[i][j] < 0:
                return False
    return True


def solve():
    AA = [a[:] for a in A]

    for _ in range(4):
        if match(AA, B):
            return True

        tmp = [[-1]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmp[j][N-1-i] = AA[i][j]
        AA = tmp
    return False


print('Yes') if solve() else print('No')
