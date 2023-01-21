N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

P -= 1
Q -= 1
R -= 1
S -= 1

PQ = A[P:Q+1]
RS = A[R:S+1]

for i in range(N):
    if P <= i <= Q:
        print(RS[i-P], end='')
    elif R <= i <= S:
        print(PQ[i-R], end='')
    else:
        print(A[i], end='')
    if N - 1 > i:
        print(' ', end='')
    else:
        print()
