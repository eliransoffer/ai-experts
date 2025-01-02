my_set = set()

weekdays = {'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'}
print(weekdays)
weekdays.add('sun')
print(weekdays)

names = ['val', 'amit', 'idan', 'amit']
print(list(set(names)))

print('sun' in weekdays)
print('a' in 'hello')
print('val' in names)

winter_games = ['athens', 'los angeles']
summer_games = ['athens', 'paris']

print(set(winter_games).intersection(set(summer_games)))
print(set(winter_games).union(set(summer_games)))
print(set(winter_games).difference(set(summer_games)))
print(set(winter_games) - set(summer_games))