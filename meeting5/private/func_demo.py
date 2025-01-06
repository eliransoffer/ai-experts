def add_one(num):
    print("inside add_one")
    return num + 1

ret_val = add_one(6)

a = 6

print(add_one)
my_foo = add_one
print(my_foo)
print(my_foo(9))

def my_sum(n1, n2):
    return n1 + n2

def my_mul(n1, n2):
    return n1 * n2

def perform_calc(num1, num2, action_func):
    return action_func(num1, num2)

perform_calc(5, 6, my_sum)


