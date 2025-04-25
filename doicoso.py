a = int(input())
for _ in range(a):
    n, b = map(int, input().split())
    s: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r = ""
    while n != 0:
        r += s[int(n % b)]
        n = n // b
    print(r[::-1])