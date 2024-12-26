
n = 10
a = 4
def calc_age(n):
    global a
    print(a)
    a = 3
    if n == 3:
        return "t"
    else:
        return 5

# print(n)

# print(calc_age)

print(calc_age(15))

print(a)

# def print():
#     print("****")