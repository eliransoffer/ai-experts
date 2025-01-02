# def add_one(num):
#     return num + 1
#
# def add_one():
#     return 1

def add_one(a, b, c=None, num=0):
    print(a, b, c, num)
    return num + 1

print(add_one(4, 5, num=70))
print(add_one(num=70, a=5, c=6, b=8))

print("rrr", "sdfsdf", "sdfsdf")


# def print_names(special_char, *names):
#     print(special_char)
#     print(names)

# print_names("Valeria", "Amit", "Avi")
# print_names()

def print_names(special_char, *names, print_star=False, **other_params):
    print(special_char)
    print(names)
    if print_star:
        print("*")
    print(other_params)

print_names("$",print_star=False, city="Tel Aviv", country="Israel")