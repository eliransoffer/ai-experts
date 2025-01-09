from pprint import pprint

word = "sun"

def add_km(c, km):
    c["km"] += km

class Car:
    def __init__(self, manufacturer, model, color):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.km = 0

    # reset

car1 = Car("mazda", "3", "white")
print(car1.color)

# if __name__ == '__main__':
#     car = {
#         "manufacturer": "mazda",
#         "model": "3",
#         "year": 2015,
#         "color": "white",
#         "km": 150000,
#         "fuel": 60
#     }
#     add_km(car, 1)
#     pprint(car)