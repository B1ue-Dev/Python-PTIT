class Nhanvien:
    def __init__(self, ten, id, lt, th):
        if lt > 10:
            lt /= 10
        if th > 10:
            th /= 10
        self.ten = ten
        self.id = id
        self.tb = (lt + th) / 2
        if self.tb < 5:
            self.stt = "TRUOT"
        elif self.tb < 8:
            self.stt = "CAN NHAC"
        elif self.tb <= 9.5:
            self.stt = "DAT"
        else:
            self.stt = "XUAT SAC"

    def __str__(self):
        return f"{self.id} {self.ten} {self.tb:.2f} {self.stt}"

ds = []

for i in range(int(input())):
    ten = input().strip()
    lt = float(input())
    th = float(input())
    _id = ''
    _id += 'TS0' + str(i + 1)
    ds.append(Nhanvien(ten, _id, lt, th))

ds.sort(key=lambda x: x.tb, reverse=True)

for nv in ds:
    print(nv)