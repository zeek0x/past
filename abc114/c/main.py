from collections import deque

N = int(input())

ans = 0

Q = deque()
Q.append((3, (True, False, False)))
Q.append((5, (False, True, False)))
Q.append((7, (False, False, True)))


i = 0
while True:
    i, flag = Q.popleft()
    if i > N:
        break

    if all(f for f in flag):
        ans += 1
    Q.append((10*i+3, (True, flag[1], flag[2])))
    Q.append((10*i+5, (flag[0], True, flag[2])))
    Q.append((10*i+7, (flag[0], flag[1], True)))

print(ans)
