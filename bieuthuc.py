a = int(input())
l = []
for _ in range(a):
    tc = input()
    l.append(tc)

for i in l:
    stack = []
    cnt = 0
    res = []
    for idx, c in enumerate(i):
        if c == '(':
            cnt += 1
            stack.append(cnt)
            res.append(cnt)
        elif c == ')':
            res.append(stack.pop())
    print(" ".join([str(j) for j in res]))