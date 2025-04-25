def main():
    a = int(input())
    over3 = []
    nums = input()
    l = list(nums.split())

    _min = min(l)
    _max = max(l)

    new_list = []
    for i in l:
        if i != _min and i != _max:
            new_list.append(i)

    total = float(0)
    for i in new_list:
        total += float(i)

    avg = total / len(new_list)

    print(round(avg, 2))

if __name__ == "__main__":
    main()