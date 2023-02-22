import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = bisect.bisect_left(A, K)

print(-1) if ok == N else print(ok)
