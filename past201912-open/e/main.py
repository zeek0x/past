N, Q = map(int, input().split(' '))
E = [[False for _ in range(N)] for _ in range(N)]
S = [list(map(int, input().split(' '))) for _ in range(Q)]

for s in S:
    if s[0] == 1:
        a = s[1] - 1
        b = s[2] - 1
        E[a][b] = True
    elif s[0] == 2:
        a = s[1] - 1
        for i in range(N):
            if E[i][a]:
                E[a][i] = True
    elif s[0] == 3:
        a = s[1] - 1
        F = []
        for i in range(N):
            if E[a][i]:
                for j in range(N):
                    if E[i][j]:
                        F.append((a, j))
        for (a, j) in F:
            E[a][j] = True

for i in range(N):
    for j in range(N):
        if i == j:
            print('N', end='')
        else:
            print('Y', end='') if E[i][j] else print('N', end='')
    print()
