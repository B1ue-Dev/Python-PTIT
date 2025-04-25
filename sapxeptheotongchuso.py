T = int(input())
tcs = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    tcs.append(A)
for i in tcs:
    def sumnum(n):
        return sum(int(i) for i in str(n))

    sorted_l = sorted(i, key=lambda x: (sumnum(x), x))
    print(" ".join([str(j) for j in sorted_l]))
