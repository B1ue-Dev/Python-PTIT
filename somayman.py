def main():
    a = input()
    num4 = 0
    num7 = 0
    if len(a) > 18:
        print("NO")
    else:
        for char in a:
            if char == "4":
                num4 += 1
            elif char == "7":
                num7 += 1
        if num4 + num7 == 7 or num4 + num7 == 4:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()