a = int(input())
l = []
for _ in range(a):
    tc = int(input())
    l.append(tc)

def hamming(n):
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i
    return n == 1

for i in l:
    if i == 1:
        print(1)
    elif not hamming(i):
        print("Not in sequence")
    else:
        dp = [1]
        i2 = i3 = i5 = 0

        while dp[-1] < i:
            nextval = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp.append(nextval)
            if nextval == dp[i2] * 2:
                i2 += 1
            if nextval == dp[i3] * 3:
                i3 += 1
            if nextval == dp[i5] * 5:
                i5 += 1

        print(dp.index(i) + 1)
