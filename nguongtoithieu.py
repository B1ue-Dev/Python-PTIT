inp = input()
cnt = int(input())
res = {}
while inp != "":
    fd = inp[:2]
    if len(fd) == 2:
        if fd not in res.keys():
            res[fd] = 1
        else:
            res[fd] += 1
    inp = inp[2:]

# print(" ".join(sorted(x for x in res)))
checked = False
for i in sorted(res.keys()):
    if res[i] >= cnt:
        print(i, res[i])
        checked = True
if not checked:
    print("NOT FOUND")