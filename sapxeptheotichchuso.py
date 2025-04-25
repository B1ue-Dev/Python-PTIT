T = int(input())
tcs = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    tcs.append(A)
for i in tcs:
    def tichnum(n):
        r = 1
        for j in str(n):
            r *= int(j)
        return r

    sorted_l = sorted(i, key=lambda x: (tichnum(x), x))
    print(" ".join([str(j) for j in sorted_l]))
