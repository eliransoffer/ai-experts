# dict as mapper
def map_names():
    d = {}
    while True:
        name = input("insert name: ")
        if name == '$':
            break
        # normalization
        name = name.lower()
        # option 1
        if name not in d:
            d[name] = 1
        # option 2
        # if d.get(name):
        else:
            d[name] += 1
    return d

# dict as object
def input_persons():
    # ret_val = [
    #     {
    #         "name": "val",
    #         "id": "123",
    #         "birth_year": 1987
    #     },
    #     {
    #         "name": "yaniv",
    #         "id": "234",
    #         "birth_year": 1988
    #     }
    # ]

# print(map_names())
#     ret_val = {
#         "123": {"name":'val', "id": "123", "year": 1987},
#         "234": {}
#     }
    ret_dict = {}
    while True:
        user_input = input("Insert data: ")
        if user_input == "$":
            break
        pid, name, year = user_input.split(",")
        person = {
            "id": pid,
            "name": name,
            "year": int(year)
        }
        ret_dict[pid] = person
        # ret_dict[pid] = {
        #     "id": pid,
        #     "name": name,
        #     "year": int(year)
        # }
    return ret_dict

print(input_persons())

