def reverse(num: int):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a = int(input())
    l: list[int] = []
    for i in range(0, a):
        tc = int(input())
        l.append(tc)

    for i in range(0, a):
        if gcd(l[i], reverse(l[i])) == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()