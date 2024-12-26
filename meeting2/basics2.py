# + - / * ** % //

# modulus - remainder
print(5 % 2)
# div - the whole part
print(5 // 2)

minutes = 103
# 01:43

print(f"{minutes // 60:02d}:{minutes % 60:02d}")

my_bool = True
my_bool2 = False

# > < == != >= <=
b = 5 < 2
print(b)

# logical operators
print(b and False)
print(b or True)
print(not b)

sentence = "The life is beautiful"
print(sentence[4])
# slicing
print(sentence[4:10])
# striding
print(sentence[4:10:2])

print(sentence[5:])
print(sentence[:5]) #[0:5]

print(sentence[-5])
print(sentence[-1])
print("-------")
print(sentence[-1::-1])
print(sentence[-1:-5:-1])
print(sentence[::-1])

l1 = [1, 2, 3, 4]
print(l1[2])
l2 = [
    1,
    "sun",
    3.5,
    True,
    "rrrr"
]
print(l2)

# sentence[2] = "t" # not working - string is immutable
# sentence = None

l2[1] = "sky"
print(l2)

words = sentence.split()
print(words)
print(words[::-1])

print(list(sentence))

reverse_words = words[::-1]
reverse_words[0] = "***"
print(reverse_words)
print(" ".join(reverse_words))
print("".join(reverse_words))

l3 = [
    "valeria",
    "erez",
    "yaniv",
    [4, 5, [6]]
]
# l3[0][0] = "t"
print(l3[-1][0])
print(l3[-1][-1][-1])

# r = range(1, 10, 2)
r = range(1, 1_000_000_000)
print(r, type(r))

print(r.index(5))

print("life" in sentence)
print("rrr" in l3)
print(677 in r)

r2 = range(100, 10, -5)

for elem in l3:
    print(elem)

for char in sentence:
    print(char)
i = "tedi"
for i in range(10, 0, -1):
    x = "ron"
    print(i)
    print(i+1)

print(i)
print(x)

num = 10
while num < 15:
    print("***")
    num += 1

data = []
while True:
    i = input("insert:")
    if i == "*":
        break
    data.append(i)
print(data)

weather = input("insert weather:")

if weather == "sun":
    print("take sunglasses")
elif weather == "rain":
    print("take umbrella")
elif weather == "snow":
    print("take coat")
else:
    print("Take nothing")

match weather:
    case "sun" | "rain":
        print("")
    case "rain":
        pass




