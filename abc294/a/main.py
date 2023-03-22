N = int(input())
l = [str(i) for i in map(int, input().split()) if i % 2 == 0]
print(' '.join(l))
