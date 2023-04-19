from collections import defaultdict

N = int(input())
Q = int(input())

boxes = [[] for _ in range(N+1)]
cards = defaultdict(list)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        card = query[1]
        box = query[2]
        boxes[box].append(card)
        cards[card].append(box)
    elif query[0] == 2:
        box = query[1]
        boxes[box].sort()
        print(*boxes[box])
    elif query[0] == 3:
        card = query[1]
        cards[card].sort()
        print(*sorted(list(set(cards[card]))))
