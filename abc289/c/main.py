import itertools

N, M = map(int, input().split())
C = []
A = []

for _ in range(M):
    c = int(input())
    C.append(c)
    a = list(map(int, input().split()))
    a_val = 0
    for i in a:
        a_val |= 1 << (i-1)
    A.append(a_val)

N_val = 0
for i in range(N):
    N_val |= 1 << i

def has_bit(n, i):
    return (n & (1 << i) > 0)

ans = 0
for i in range(1, M+1):
    for conb in itertools.combinations(A, i):
        x_val = 0
        for val in conb:
            x_val |= val
        if N_val == x_val:
            ans += 1

print(ans)
