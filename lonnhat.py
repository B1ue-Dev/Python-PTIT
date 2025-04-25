def main():
    a = int(input())
    l: list[str] = []
    for i in range(0, a):
        tc = input()
        l.append(tc)

    for i in l:
        tnum = ""
        largest = None
        for char in i:
            if char.isnumeric():
                tnum += char
            else:
                if tnum != "":
                    temp = int(tnum)
                    if largest is None or temp > largest:
                        largest = temp
                    tnum = ""
        if tnum != "":
            temp = int(tnum)
            if largest is None or temp > largest:
                largest = temp
        print(largest)

# Forced to have this
if __name__ == "__main__":
    main()
