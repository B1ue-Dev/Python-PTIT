inp = input()
res = set()
while inp != "":
    if len(inp[:2]) == 2:
        res.add(inp[:2])
    inp = inp[2:]

print(" ".join(sorted(x for x in res)))