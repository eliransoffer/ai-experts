def foo():
    vals = []
    while True:
        i = input("Name")
        if i == "@":
            break
        vals.append(i)
    return vals


r = foo()