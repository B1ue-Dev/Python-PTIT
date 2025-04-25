import math
def reverse(num: int):
    return int(str(num)[::-1])

def songuyento(num: int):
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    a = int(input())
    inputs = [int(input()) for _ in range(a)]

    for limit in inputs:
        primes = []
        prime_set = set()

        for num in range(13, limit):
            if songuyento(num):
                primes.append(num)
                prime_set.add(num)

        visited = set()
        result = []
        for p in primes:
            rev = reverse(p)
            if p not in visited and rev in prime_set and rev != p:
                result.append(p)
                result.append(rev)
                visited.add(p)
                visited.add(rev)

        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()