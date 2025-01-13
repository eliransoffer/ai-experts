import datetime


now = datetime.datetime.now()
print(now)
utc_now = datetime.datetime.utcnow()
print(utc_now)

today = datetime.date.today()
print(today)

bday = datetime.datetime(2025, 2, 11)
print(bday)
d = bday - now
print(type(d))
print(d)

# t = bday + now

t = now + datetime.timedelta(days=365)
print(t)



print(now.replace(year=now.year + 1))

print(now.strftime("%d/%m/%Y, %A"))

d1 = "2/11/87 12:30"
date_obj = datetime.datetime.strptime(d1, "%m/%d/%y %H:%M")
print(date_obj)

print(now.weekday())
