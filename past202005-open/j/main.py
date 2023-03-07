import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * N

for a in A:
    k = bisect.bisect_right(B, -a)
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a
