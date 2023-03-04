N = int(input())

def divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = 0
for n in range(1, (N+1)//2):
    ans += len(divisors(n)) * len(divisors(N-n))
ans *= 2

if N % 2 == 0:
    ans += len(divisors(N//2)) ** 2

print(ans)
