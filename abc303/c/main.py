import bisect

N, M, H, K = map(int, input().split())
S = input()
XY = []
for _ in range(M):
    x, y = map(int, input().split())
    XY.append((x, y))

XY.sort(key=lambda xy: (xy[0], xy[1]))
X = [xy[0] for xy in XY]
used = [False for _ in range(M)]

x = 0
y = 0
ok = True
for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1

    H -= 1

    if H < 0:
        ok = False
        break

    if K > H:
        xl = bisect.bisect_left(X, x)
        xr = bisect.bisect_right(X, x)
        for j in range(xl, xr):
            if (not used[j]) and XY[j][0] == x and XY[j][1] == y:
                used[j] = True
                H = K


print("Yes") if ok else print("No")
