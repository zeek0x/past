N, K = map(int, input().split())
S = input()

cnt = 0
ans = []
for s in S:
    if cnt < K and s == 'o':
        cnt += 1
        ans.append('o')
    else:
        ans.append('x')

print(''.join(ans))
