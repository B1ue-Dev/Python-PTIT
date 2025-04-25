a = [143, 43, 22, 99, 7, 9, 1111, 10000000]
b = {}
for i in a:
    b[i] = sum(int(j) for j in str(i))
def comp(x,y):
    if x > y and b[x] > b[y]:
