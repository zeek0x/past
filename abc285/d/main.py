N = int(input())
S = []
T = []
M = {}


def is_circuit(s, t, M):
    while True:
        if t not in M:
            return False
        if s == t:
            return True
        tt = t
        t = M[t]
        del M[tt]


for _ in range(N):
    s, t = input().split(' ')
    M[s] = t
    S.append(s)
    T.append(t)

ok = True
for i in range(N):
    if is_circuit(S[i], T[i], M):
        ok = False
        break

print('Yes') if ok else print('No')
