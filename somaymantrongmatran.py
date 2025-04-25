N, M = map(int, input().split())
max_val = -1
min_val = 10001
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    max_val = max(max_val, max(row))
    min_val = min(min_val, min(row))
smm = max_val - min_val
found = False
pos = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == smm:
            found = True
            pos.append((i, j))
if found:
    print(smm)
    for i, j in pos:
        print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")