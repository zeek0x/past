N, Q = map(int, input().split())
players = [0] * N

for _ in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        players[event[1]-1] += 1
    elif event[0] == 2:
        players[event[1]-1] += 2
    elif event[0] == 3:
        print('Yes') if players[event[1]-1] >= 2 else print('No')
