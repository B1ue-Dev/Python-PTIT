def main():
    a = int(input())
    l: list[str] = []
    for i in range(0, a):
        tc = input()
        l.append(tc)

    for i in l:
        ifip = True
        a = i.split(".")
        if len(a) != 4:
            ifip = False
        else:
            for n in a:
                if not n.isdigit():
                    ifip = False
                    break
                if not 0 <= int(n) <= 255:
                    ifip = False
                    break
        if ifip:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()