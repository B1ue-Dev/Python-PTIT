import sys

data = sys.stdin.read().splitlines()
t = int(data[0])
tests = data[1:t+1]

for i in tests:
    if len(i) <= 1:
        print("NO")
    else:
        res = 0
        for num in i: res += int(num)
        if len(str(res)) <= 1: print("NO")
        else: print("YES" if str(res) == str(res)[::-1] else "NO")