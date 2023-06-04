N = int(input())
W = input().split()
ok = any([w in ['and', 'not', 'that', 'the', 'you'] for w in W])
print('Yes') if ok else print('No')
