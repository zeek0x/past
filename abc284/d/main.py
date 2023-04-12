T = int(input())

for _ in range(T):
    N = int(input())
    i = 2
    while True:
        if N % i == 0:
            pq = i
            break
        i += 1
    if N % pq**2 == 0:
        p = pq
        q = N // p**2
    else:
        q = pq
        p = int((N // pq)**(1/2))
    print(p, q)
