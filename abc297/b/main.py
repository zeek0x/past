S = input()
B = (S.find('B') + S.rfind('B')) % 2 != 0
K = S.find('R') < S.find('K') < S.rfind('R')
ok = B and K
print('Yes') if ok else print('No')
