import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate(p1: Point, p2: Point):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

a = int(input())
l = []
for _ in range(a):
    tc = list(map(float, input().split()))
    l.append(tc)

for i in l:
    x1, y1, x2, y2 = map(float, i)
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    print(f"{calculate(p1, p2):.4f}")