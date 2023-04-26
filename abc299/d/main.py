N = int(input())

l = 1
r = N

while True:
    i = (l+r) // 2
    print('? '+str(i))
    p = input()
    if p == '0':
        l = i
    else:
        r = i

    if l < r-1:
        continue

    print('! '+str(l))
    break
