def main():
    a = int(input())
    l: list[str] = []
    for i in range(0, a):
        tc = input()
        l.append(tc)

    for i in l:
        tnum = ""
        smallest = None
        for char in i:
            if char.isnumeric():
                tnum += char
            else:
                if tnum != "":
                    temp = int(tnum)
                    if smallest is None or temp < smallest:
                        smallest = temp
                    tnum = ""
        if tnum != "":
            temp = int(tnum)
            if smallest is None or temp < smallest:
                smallest = temp
        print(smallest)

# Forced to have this
if __name__ == "__main__":
    main()
