T = int(input())
for _ in range(T):
    input()
    print(len([i for i in map(int, input().split()) if i % 2 == 1]))
