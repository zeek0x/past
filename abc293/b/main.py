N = int(input())
A = [0] + list(map(int, input().split()))

notCalled = set(range(1, N+1))

for i in range(1, N+1):
    if i in notCalled and A[i] in notCalled:
        notCalled.remove(A[i])

L = sorted(list(notCalled))
print(len(L))
print(' '.join(map(str, L)))
