def main():
    a = int(input())
    inputs = [int(input()) for _ in range(a)]

    for t in inputs:
        num = list(str(t))
        for i in range(len(num) - 1, 0, -1):
            if int(num[i]) >= 5:
                num[i] = '0'
                num[i-1] = str(int(num[i-1]) + 1)
            elif int(num[i]) < 5:
                num[i] = '0'

        print("".join(x for x in num))

if __name__ == "__main__":
    main()