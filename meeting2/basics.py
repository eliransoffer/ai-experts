print("Hello")
num = 4
print(type(num))
num = 5.6
print(type(num))
word = "Sun"
print(type(word))

print(num + 5)

name = input("Insert your name: ")
print(name)

year = int(input("Your birth year: "))
print(year)
print(type(year))

y1 = '1987'
y2 = 1987

# creates multiple strings by adding new word each time - not efficient
print(name + " you are " + str(2024 - year) + " years old")

# efficient - does not create many strings
print(name, "you are", 2024 - year, "years old", sep="_", end="\n\n")

# creates one long string
print(f"{name} you are {2024 - year} years old")

s1 = name, "you are", 2024 - year, "years old"
print(s1)

sentence1 = "The sky is blue"
sentence2 = 'The sky is blue'

sentence3 = 'She said: "The sky is blue"'
text = """
Line 1
Line 2
"""
print(text)

text = '''
Line 1
Line 2
'''

text3 = f'''
Line 1 {name}
Line 2
'''