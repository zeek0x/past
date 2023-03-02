from collections import deque
from collections import defaultdict

Q = int(input())

que = deque()

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        C, X = query[1], int(query[2])
        que.append((C, X))
    elif query[0] == '2':
        D = int(query[1])
        delete = defaultdict(int)
        while D > 0 and len(que) > 0:
            C, X = que.popleft()
            if X >= D:
                delete[C] += D
                que.appendleft((C, X-D))
            else:
                delete[C] += X
            D -= X
        print(sum([v*v for v in delete.values()]))
