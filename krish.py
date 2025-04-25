def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)

def main():
    a = int(input())
    l: list[int] = []
    for i in range(a):
        tc = int(input())
        l.append(tc)

    for i in range(a):
        total = 0
        for j in str(l[i]):
            total += giaiThua(int(j))

        if int(total) == l[i]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()