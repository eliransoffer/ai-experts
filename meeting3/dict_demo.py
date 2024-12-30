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

