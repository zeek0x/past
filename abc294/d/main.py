N, Q = map(int, input().split())

nc = 1
nr = 1

checked = [False]*(N+1)

for _ in range(Q):
    event = input().split()
    if event[0] == '1':
        nc += 1
    elif event[0] == '2':
        x = int(event[1])
        checked[x] = True
        if nr == x:
            for i in range(nr, N+1):
                if not checked[i]:
                    nr = i
                    break
    elif event[0] == '3':
        print(nr)
