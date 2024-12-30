l = [1,2,3]
l = []
l.append("fff")
l1 = list()
print(len("djfhgldsjfkghd"))
print(len(l1))
l2 = [3,4,5,7]
print(len(l2))
print(min(l2))
print(max(l2))
sorted_list = sorted(l2, reverse=True)
print(sorted_list)
print(f"l2: {id(l2)}")
print(f"sorted_list: {id(sorted_list)}")

print(f"l2[0]: {id(l2[0])}")
print(f"sorted_list[-1]: {id(sorted_list[-1])}")

num = 3
print(f"num: {id(num)}")
a = num

num += 1
print(f"num: {id(num)}")
print(f"a: {id(a)}")

print(divmod(15, 6))

my_tuple = (1,2,3)
print(my_tuple[0])

a, b, c = my_tuple
print(b)

d, m, y = "11-02-2008".split("-")
print(y)

h, m = divmod(155, 60)
print(f"{h:02d}:{m:02d}")

months = ['jan', 'feb', 'mar', 4, 5, 6]
a, *b = months
print(f"a:{a}, *b:{b}")

a, *b, c, d = months
print(f"a:{a}, *b:{b}, c:{c}, d:{d}")

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(sum(list1))
new_list = [list1, list2]
print(new_list)
# print(sum([list1, list2]))
new_list = [*list1, *list2]
print(new_list)
# print(sum([*list1, *list2]))

for elem in "orange":
    print(elem)

word = "orange"
for i in range(len(word)):
    print(f"index: {i}, char: {word[i]}")

for i, char in enumerate(word):
    print(f"index: {i}, char:{char}")

countries = ["Israel", "US", "Germany","France"]
cities = ["Jerusalem", "Washington DC", "Berlin"]
temp = [2, -1]

# for i in range(len(countries)):
#     print(f"{countries[i]}: {cities[i]}")

for country, city, temper in zip(countries, cities, temp):
    print(f"{country}:{city}:{temper}")

