from pprint import pprint
# manufacturer = "drgdgf"

counter = 10

class Car:

    counter = 1

    def __init__(self, manufacturer, model, color, tank_capacity=50):
        self.id = Car.counter
        Car.counter += 1
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.tank_capacity = tank_capacity
        self._km = 0
        self._fuel = 0


    def __str__(self):
        return f"{self.manufacturer} | {self.model} | {self._km}"

    def __repr__(self):
        return str(self.id)
        # return self.__str__()

    def __len__(self):
        return 6

    def add_fuel(self, liters):
        if liters + self._fuel > self.tank_capacity:
            raise Exception("Exceeds tank capacity")
        self._fuel += liters


if __name__ == '__main__':
    car1 = Car("mazda", "3", "white")
    car1.color = "red"
    print(car1)
    print(car1.color)
    car2 = Car("tesla", "model S", "white")
    print((car2.color))
    # car2._km += 2
    # car2._km +=2
    # print(car2._km)
    # car2.add_fuel = print
    # car2.add_fuel("xfgdgcfgdgdfg")
    # print(car2.__km)
    # print(car2._Car__km)
    car2.add_fuel(6)
    # Car.add_fuel(car2, 5)
    print(car2)
    print("convert", str(car2))
    print(len("dsfsdfsdf"))
    print(len(car2))
    print([car1, car2])
    print(counter)
    print(Car.counter)
    print(car2.counter)
    print(car2.id)


"ddd".__str__()

# l = [1,2,3]

object