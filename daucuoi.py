def main():
    a = int(input())
    l: list[str] = []
    for i in range(0, a):
        tc = input()
        l.append(tc)

    for i in range(0, a):
        if str(l[i])[:2] == str(l[i])[-2:]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()