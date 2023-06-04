N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
pair = 0
for a in A:
    if a == pair:
        ans += 1
        pair = 0
    else:
        pair = a

print(ans)
