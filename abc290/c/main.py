N, K = map(int, input().split())
A = list(map(int, input().split()))

A = list(set(A))
A.sort()

i = 0
for a in A:
    if i < K and i == a:
        i += 1
    else:
        break

print(i)
