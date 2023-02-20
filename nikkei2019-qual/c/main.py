N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda ab: ab[0] + ab[1], reverse=True)

tk = 0
ao = 0
for i in range(len(AB)):
    if i % 2 == 0:
        tk += AB[i][0]
    else:
        ao += AB[i][1]

print(tk - ao)
