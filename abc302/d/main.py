N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = -1
n = N - 1
m = M - 1
while n >= 0 and m >= 0:
    if abs(A[n] - B[m]) <= D:
        ans = A[n] + B[m]
        break

    if A[n] > B[m]:
        n -= 1
    else:
        m -= 1

print(ans)
