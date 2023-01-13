K = int(input())
[A, B] = [int(s) for s in input().split(' ')]

ok = False
for i in range(A, B+1):
    if i % K == 0:
        ok = True
        break

print('OK') if ok else print('NG')
