inp = input()
if inp.split(".")[-1:][0].lower() == "py":
    inp = inp[:-3]
    if len(inp) <= 128:
        checked = True
        for char in inp:
            if not (char.isalpha() or char == "_" or char == "."):
                checked = False
                break
        if checked:
            print("yes")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")