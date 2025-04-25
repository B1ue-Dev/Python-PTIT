def main():
    a = int(input())
    if a > 10:
        return
    l: list[tuple] =  []
    for _ in range(a):
        name = input()
        bs = list(map(int, input().split()))
        l.append((name, bs[0], bs[1]))

    ls = sorted(l, key=lambda index : ( -index[1], index[2], index[0] ) )
    for key in ls:
        print("{} {} {}".format(key[0], key[1], key[2]))

if __name__ == "__main__":
    main()