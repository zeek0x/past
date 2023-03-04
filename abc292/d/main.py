from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

ok = True

checked = [False] * N
for i in range(N):
    if checked[i]:
        continue

    edge_cnt = 0
    node_cnt = 0
    Q = deque()
    Q.append(i)
    checked[i] = True
    while len(Q) > 0:
        j = Q.pop()
        node_cnt += 1

        for k in edges[j]:
            edge_cnt += 1
            if checked[k]:
                continue

            checked[k] = True
            Q.append(k)

    # print(i, edge_cnt // 2, node_cnt)
    # print()
    if edge_cnt // 2 != node_cnt:
        ok = False
        break

print('Yes') if ok else print('No')
