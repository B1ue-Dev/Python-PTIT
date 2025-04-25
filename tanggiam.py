def sotanggiam(n: str):
    n = str(n)
    if len(n) < 3:
        return False

    i = 0
    while i + 1 < len(n) and n[i] < n[i+1]:
        i += 1

    if i == 0 or i == len(n) - 1:
        return False

    while i + 1 < len(n) and n[i] > n[i+1]:
        i += 1

    return i == len(n) - 1

def main():
    a = int(input())
    l: list[int] = []
    for i in range(a):
        tc = int(input())
        l.append(tc)

    for i in range(a):
        if sotanggiam(str(l[i])):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()