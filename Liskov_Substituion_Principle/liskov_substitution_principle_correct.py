"""
Лучшим варианты было бы реализовать методы setter и getter в суперклассе Car.
С их помощью мы можем устанавливать и получать свойства автомобиля, не оставляя эту реализацию последующим разработчикам.
Таким образом, мы просто получаем свойства с помощью метода setter, и его реализация остается инкапсулированной в суперклассе.

Так мы сможем соблюсти принцип подстановки Лисков, как показано ниже:
"""

class Car:
    def __init__(self, type):
        self.type = type
        self.car_properties = {}

    def set_properties(self, color, gear, capacity):
        self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

    def get_properties(self):
        return self.car_properties


class PetrolCar(Car):
    def __init__(self, type):
        self.type = type
        self.car_properties = {}


car = Car("SUV")
car.set_properties("Red", "Auto", 6)

petrol_car = PetrolCar("Sedan")
petrol_car.set_properties("Blue", "Manual", 4)

cars = [car, petrol_car]


def find_red_cars(cars):
    red_cars = 0
    for car in cars:
        if car.get_properties()['Color'] == "Red":
            red_cars += 1
    print(f'Number of Red Cars = {red_cars}')


find_red_cars(cars)