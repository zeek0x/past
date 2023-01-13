n = int(input())


def is_zorome(t):
    l = list(str(t))
    return all([x == l[0] for x in l])


i = 0
t = 0
while i < n:
    t += 1
    if is_zorome(t):
        i += 1

print(t)
