def main():
    a = int(input())
    tc = list(map(int, input().split()))

    chnum = {}
    for num in tc:
        res = 0
        for en in tc:
            if en != num:
                res += abs(en - num)
            else:
                continue
        if not list(chnum.keys()):
            chnum = {num: res}
        elif list(chnum.items())[0][1] > res:
            chnum = {num: res}
        elif list(chnum.items())[0][1] < res:
            continue

    print(list(chnum.items())[0][1], list(chnum.items())[0][0])


if __name__ == "__main__":
    main()