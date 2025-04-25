def main():
    a = int(input())
    l: list[str] =  []
    for _ in range(a):
        tc = input()
        l.append(tc)

    for i in l:
        res = ""
        for t in range(0, len(i), 2):
            res += str(i[t]) * int(i[t+1])
        print(res)

if __name__ == "__main__":
    main()