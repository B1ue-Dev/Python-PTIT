mn = input()
m = int(mn.split()[0])
n = int(mn.split()[1])

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a & b
print(" ".join(str(i) for i in sorted(c)))

d = a.difference(b)
print(" ".join(str(i) for i in sorted(d)))

e = b.difference(a)
print(" ".join(str(i) for i in sorted(e)))