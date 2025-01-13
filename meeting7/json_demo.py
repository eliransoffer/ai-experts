import json

# with open("data/fab_mock_data.json") as f:
#     content = f.read()
# print(content)
# print(type(content))
# # print(content["fabLocation"])

with open("data/fab_mock_data.json") as f:
    content = json.load(f)
print(content)
print(type(content))
print(content["fabLocation"])

s = '{"name": "Valeria"}'
obj = json.loads(s)
print(obj, type(obj))

my_dict = {
    1: "jan",
    2: ["q", 2, 4]
}

# with open("data/my_dict.json", "w") as f:
#     json.dump(my_dict, f)

with open("data/my_dict.json") as f:
    json.load(f)
