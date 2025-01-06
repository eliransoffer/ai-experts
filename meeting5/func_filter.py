
l = [10, 3, 42,3,4,5]

odd = []
for elem in l:
    if elem % 2 != 0:
        odd.append(elem)

print(odd)

def is_odd(elem):
    return elem % 2

# is_odd_2 = lambda elem: elem % 2 != 0

# print(list(filter(is_odd, l)))

# print(list(filter(lambda e: e % 2 != 0, l)))

my_filter = filter(lambda e: e % 2, l)
print(my_filter)

for elem in filter(lambda e: e % 2, l):
    print(elem)


words = ["apple", "IDAN", "SKY", "tea"]
for w in filter(str.islower, words):
    print(w)


# filter(filter_upper_words, ["hello", 'hi', "WORLD", "yes"])
# l = ["hello", 'hi', "WORLD", "yes"]
# filter_obj = filter(str.islower, l)
# print(type(filter_obj))
# print(list(filter_obj))

# filtered = []
# for elem in l:
#     if str.lower(elem):
#         filtered.append(elem)
# return filtered

# print("".join(filter(lambda c: c not in "aAeEiIoOuU", "hello")))



# filter_obj = filter(str.islower, ["hello", 'hi', "WORLD", "yes"])
# print(set(filter_obj))


