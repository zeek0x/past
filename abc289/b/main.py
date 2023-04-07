N, M = map(int, input().split())
A = list(map(int, input().split()))

l = []
r = []
a = 0
for i in range(1, N+1):
    if M > a and A[a] == i:
        r.append(i)
        a += 1
    else:
        r.append(i)
        l.extend(reversed(r))
        r = []

print(' '.join([str(i) for i in l]))
