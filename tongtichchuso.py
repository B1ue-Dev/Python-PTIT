def main():
    a = int(input())
    l: list[str] = []
    for _ in range(a):
        tc = input().strip()
        l.append(tc)

    for s in l:
        sc = 0
        sl = 1
        has_nonzero = False

        for num in range(len(s)):
            digit = int(s[num])
            if num % 2 == 0:
                sc += digit
            else:
                if digit != 0:
                    sl *= digit
                    has_nonzero = True

        if not has_nonzero:
            sl = 0

        print(f"{sc} {sl}")

if __name__ == "__main__":
    main()
