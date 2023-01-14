[N, M, Q] = list(map(int, input().split(' ')))
E = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    [u, v] = list(map(int, input().split(' ')))
    E[u-1][v-1] = E[v-1][u-1] = True

C = list(map(int, input().split(' ')))

S = []
for _ in range(Q):
    S.append(list(map(int, input().split(' '))))

for s in S:
    if s[0] == 1:
        x = s[1]
        c = C[x-1]
        print(c)
        for i in range(N):
            if E[x-1][i]:
                C[i] = c
    elif s[0] == 2:
        x = s[1]
        print(C[x-1])
        C[x-1] = s[2]
