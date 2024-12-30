my_dict = {
    'israel': 'jerusalem',
    'france': 'paris',
    'germany': 'berlin',
    1: 'jan',
    4.5: True
}
print(my_dict['france'])
# print(my_dict['aaa'])
print(my_dict.get("aaa"))
my_dict['US'] = 'Washington DC'
print(my_dict)
my_dict[1] = 5
print(my_dict)
my_dict.pop(1)
print(my_dict)
num = 4
del my_dict['france']
# my_dict.update({'US': 'Washington'})
# l = [1,2,3,5]

grades = {
    "Moshe": [90, 87, 67],
    "Yanay": [100]
}
print(grades["Moshe"][0])

companies = {
    "Tesla": {
        "CEO": {
            "name": "Elon Mask",
            "birth_year": 1970
        },
        "employees": 10_000
    },
    "Microsoft": {
        "CEO": {
            "name": "Bla bla",
            "birth_year": 1967
        },
        "employees": 120_000
    }
}

print(companies["Tesla"]["CEO"]["birth_year"])