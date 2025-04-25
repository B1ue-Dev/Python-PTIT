def main():
    nk = list(map(int, input().split()))
    k = nk[1]

    a = sorted(list(map(int, input().split())))
    s = 1
    for i in range(1, len(a)):
        if a[i] - a[i-1] > k:
            s +=1
    print(s)

if __name__ == "__main__":
    main()
