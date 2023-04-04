N = int(input())
X = list(map(int, input().split()))
X = sorted(X)[N:-N]

print('{:.15f}'.format(sum(X)/len(X)))
