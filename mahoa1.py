def main():
    a = int(input())
    l: list[str] =  []
    for _ in range(a):
        tc = input()
        l.append(tc)

    for i in l:
        res = ""
        cnt = 0
        curchar = ""
        for char in i:
            if curchar == "":
                curchar = char
                cnt += 1
            elif char == curchar:
                cnt += 1
            elif char != curchar:
                res += f"{cnt}{curchar}"
                curchar = char
                cnt = 1
        res += f"{cnt}{curchar}"
        print(res)

if __name__ == "__main__":
    main()
