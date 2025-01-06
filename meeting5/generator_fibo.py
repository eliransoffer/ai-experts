def fibonacci_generator():
    """A generator to produce Fibonacci numbers."""
    a, b = 0, 1
    while True:  # Infinite sequence
        yield a
        a, b = b, a + b


# Using the generator
# fib_gen = fibonacci_generator()


# for elem in fib_gen:
#     print(elem)
#     if elem > 10_000:
#         break


# def fibonacci_generator(max_num):
#     """A generator to produce Fibonacci numbers."""
#     a, b = 0, 1
#     while a <= max_num:
#         yield a
#         a, b = b, a + b
#
#
# for i in fibonacci_generator(10_000):
#     print(i)
