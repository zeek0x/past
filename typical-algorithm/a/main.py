N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = N
ng = -1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if A[mid] >= K:
        ok = mid
    else:
        ng = mid

print(-1) if ok == N else print(ok)
