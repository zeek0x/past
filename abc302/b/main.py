H, W = map(int, input().split())
S = [input() for _ in range(H)]

T = "snuke"


def eq(i, j, s):
    if i < 0 or H <= i or j < 0 or W <= j:
        return False
    return S[i][j] == s


def find(i, j):
    vector = [
        [(i + t, j) for t in range(len(T))],
        [(i + t, j + t) for t in range(len(T))],
        [(i, j + t) for t in range(len(T))],
        [(i - t, j + t) for t in range(len(T))],
        [(i - t, j) for t in range(len(T))],
        [(i - t, j - t) for t in range(len(T))],
        [(i, j - t) for t in range(len(T))],
        [(i + t, j - t) for t in range(len(T))],
    ]
    for v in vector:
        l = []
        for k in range(len(v)):
            ii, jj = v[k]
            if eq(ii, jj, T[k]):
                l.append((ii, jj))
            else:
               break
        if len(l) == len(T):
            return l
    return []


for i in range(H):
    for j in range(W):
        l = find(i, j)
        if len(l) == len(T):
            [print(ii+1, jj+1) for (ii, jj) in l]
            break
