import string


def is_match(T, S, TL, SL):
    for i in range(SL - TL + 1):
        ok = True
        for j in range(TL):
            if T[j] != '.' and T[j] != S[i+j]:
                ok = False
                break
        if ok:
            return True
    return False


S = input()
SL = len(S)

C = string.ascii_lowercase + '.'

M = []

for c1 in C:
    if is_match(c1, S, 1, SL):
        M.append(c1)

for c1 in C:
    for c2 in C:
        if is_match(c1+c2, S, 2, SL):
            M.append(c1+c2)

for c1 in C:
    for c2 in C:
        for c3 in C:
            if is_match(c1+c2+c3, S, 3, SL):
                M.append(c1+c2+c3)

print(len(M))
