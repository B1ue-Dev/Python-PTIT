import math

def songuyento(num: int):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main():
    a = int(input())
    if a > 10:
        return
    l: list[str] =  []
    for _ in range(a):
        tc = input()
        l.append(tc)

    for i in l:
        checked = True
        for idx, num in enumerate(i):
            chu_so = int(num)
            if songuyento(idx) and songuyento(chu_so): continue
            if not songuyento(idx) and not songuyento(chu_so): continue
            checked = False
            break
        print("YES" if checked else "NO")
if __name__ == "__main__":
    main()

