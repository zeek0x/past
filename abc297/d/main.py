A, B = map(int, input().split())

cnt = 0

while A != B:
    if A > B:
        cnt += A // B
        A = A % B
        if A == 0:
            cnt -= 1
            break
    else:
        cnt += B // A
        B = B % A
        if B == 0:
            cnt -= 1
            break

print(cnt)
