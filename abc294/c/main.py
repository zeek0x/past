N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10 ** 9 + 1
A.append(INF)
B.append(INF)

ai = 0
bi = 0
ci = 1
ansA = []
ansB = []
while N > ai or M > bi:
    a = A[ai]
    b = B[bi]
    if a < b:
        ansA.append(ci)
        ai += 1
    else:
        ansB.append(ci)
        bi += 1
    ci += 1

for i in range(N-1):
    print(ansA[i], end=' ')
print(ansA[N-1])

for i in range(M-1):
    print(ansB[i], end=' ')
print(ansB[M-1])
