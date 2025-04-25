a = input()
while len(a) % 3 != 0:
    a = "0" + a
res = ""
for i in range(0, len(a), 3):
    r = int(a[i:i+3], 2)
    res += str(r)
print(res)