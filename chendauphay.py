def main():
    a = input()
    res = ""
    while len(a) > 3:
        res = "," + a[-3:] + res
        a = a[:-3]
    res = a + res
    print(res)

if __name__ == "__main__":
    main()