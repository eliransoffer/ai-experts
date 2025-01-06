colors = ['white', 'black', 'grey', 'red', 'green']
#
upper_colors = []
for c in colors:
    upper_colors.append(c.upper())

colors = [c.upper() for c in colors]

# {'w': 'white', 'b': 'black'}
my_dict = {}
for c in colors:
    my_dict[c[0]] = c

my_colors_dict = {c[0]: c for c in colors}
#
colors = ['white', 'black', 'grey', 'red', 'green', '']
my_colors_dict = {c: c[0] if len(c) else "" for c in colors}

print(my_colors_dict)

names = ["val", "ilan", "itay"]
grades = [90, 78, 89]

d = {n: [g] for n, g in zip(names, grades)}
print(d)

d1 = {n: i+1 for i, n in enumerate(names)}
print(d1)


#
# my_colors_dict = {}
# for c in colors: #""
#     if len(c) > 0:
#         my_colors_dict[c] = c[0]
#     else: # c = ""
#         my_colors_dict[c] = ""
#
# # d = {'a':1, 'b':2, 'c':3}
# # d.get('d')
#
# d2 = {3: "ewre", 4:"", 5:[], 6:{}, 7:None, 8:10}
# # ("", [], {}, None)
#
# for key, value in d2.items():
#     if value is None or len(value) == 0:
#         # value is empty
#
# temp = 20
# weather = 'hot' if temp > 25 else 'cool'
#
# upper_colors = []
# for c in colors:
#     upper_colors.append(c.upper())
#
# num2idx = {n: i for i, n in enumerate(nums)}
#
# num2idx = {}
# for i, n in enumerate(nums):
#     num2idx[n] = i