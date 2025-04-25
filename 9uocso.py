import math

N = int(input())
cnt = 0
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, int(math.sqrt(N))+1):
    if is_prime(i):
        primes.append(i)

for i in primes:
    if i ** 8 <= N:
        cnt += 1

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if (primes[i] ** 2) * (primes[j] ** 2) <= N:
            cnt += 1
        else:
            break

print(cnt)