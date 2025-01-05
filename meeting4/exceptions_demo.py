# def add_one(num):
#     try:
#         return num + 1
#     except:
#         print("Error occurred")
#     print('Bye')
#
#
# ret = add_one("sdfsfsdf")
# print("ret", ret)
# print(ret / 5)


def add_one(num):
    return num + 1


try:
    ret = add_one("sdfsfsdf")
    print("ret", ret)
    print(ret / 5)
except:
    print("error")

d = {'a': 1, 'b': 2}
# print(d['c'])

# print(5/0)

# 01:32
def get_minutes():
    while True:
        try:
            user_input = input("Insert hh:mm\n")
            h, m = user_input.split(":")
            h, m = int(h), int(m)
            if m > 59:
                raise Exception("Minutes must be less then 60")
                # return
            return h*60 + m
        except ValueError:
            print("You have to provide numbers separated by :", h)
        except Exception as e:
            print("The format is wrong, insert again", e, type(e))

print(get_minutes())