from collections import deque
from copy import copy

N, X = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A, B = zip(*sorted(zip(A, B)))


Q = deque()


def append(XX, BB):
    for i in range(N):
        if XX >= A[i] and BB[i] > 0:
            BBB = list(copy(BB))
            BBB[i] -= 1
            Q.append((XX-A[i], BBB))


ok = False

append(X, B)
while len(Q) > 0:
    XX, BB = Q.popleft()
    if XX == 0:
        ok = True
        break
    elif XX < 0:
        continue

    append(XX, BB)

print('Yes') if ok else print('No')
