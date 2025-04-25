a = ""
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while a != '0':
    a = input()
    if a == '0':
        break
    k, s = a.split()
    res = ""
    for c in s:
        idx = P.index(c)
        res += P[(idx + int(k)) % 28]
    print(res[::-1])