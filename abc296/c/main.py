import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ok = False
for i in range(N-1, -1, -1):
    j = bisect.bisect_left(A, A[i]-X)
    if j < N and A[i] - A[j] == X:
        ok = True
        break

print('Yes') if ok else print('No')
