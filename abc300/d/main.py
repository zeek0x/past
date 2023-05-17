def sieve(N):
    """
    Sieve of Erastosthenes
    """
    table = [0] * (N + 1)

    for i in range(2, N + 1):
        if table[i] != 0:
            continue
        for j in range(i, N + 1, i):
            if table[j] == 0:
                table[j] = i

    return [i for i in range(2, N + 1) if table[i] == i]


N = int(input())

T = sieve(3 * 10**5)
M = len(T)
ans = 0
for i in range(M - 2):
    a = T[i]
    if a**5 > N:
        break
    for j in range(i + 1, M - 1):
        b = T[j]
        if a**2 * b**3 > N:
            break
        for k in range(j + 1, M):
            c = T[k]
            if a * a * b * c * c > N:
                break
            ans += 1

print(ans)
