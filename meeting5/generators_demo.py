def fibonacci_generator(limit=1_000_000):
    print("inside fibonacci_generator")
    """A generator to produce Fibonacci numbers."""
    a, b = 0, 1
    while a <= limit:  # Infinite sequence
        yield a
        a, b = b, a + b
    print('finished generator')


l1 = [2,3,4]
l2 = [2,5,6]

l1 = list([2,3,4])
l2 = list([4,5,6])

my_gen = fibonacci_generator()
my_gen1 = fibonacci_generator(5_000)
print(my_gen)
for elem in my_gen:
    print(elem)

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# print("blabla")
#
# print(next(my_gen))
#
# for elem in my_gen:
#     print(elem)
#     break

l1 = [2,3,4]
l2 = [4,5,6]

for i in l1:
    print(i)

for j in l2:
    print(i)