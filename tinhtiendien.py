a = int(input())
l = []
for _ in range(a):
    b = []
    name = input()
    b.append(name)
    so = input()
    for i in so.split():
        b.append(i)
    l.append(b)

res = []
for idx, i in enumerate(l):
    ikh = []
    sokh = idx + 1
    name = ' '.join(word.capitalize() for word in i[0].split())
    sokhachhang = f"""KH{"0"+f"{sokh}" if sokh < 10 else sokh}"""

    a = {
        "A": 100,
        "B": 500,
        "C": 200
    }
    dinhmuc = 0
    vuot = 0
    vat = 0
    tong = 0
    if int(i[3]) - int(i[2]) < a[i[1]]:
        dinhmuc = (int(i[3]) - int(i[2])) * 450
        tong = dinhmuc
    else:
        dinhmuc = a[i[1]] * 450
        vuot = ((int(i[3]) - int(i[2])) - a[i[1]]) * 1000
        vat = vuot // 20
        tong = dinhmuc + vuot + vat

    ikh.append(sokhachhang)
    ikh.append(name)
    ikh.append(dinhmuc)
    ikh.append(vuot)
    ikh.append(vat)
    ikh.append(tong)
    res.append(ikh)

res.sort(key=lambda x : x[5], reverse=True)

for i in res:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")