import random


class Fabric(object):
    cars_created = 0

    def __init__(self):
        pass

    def make_car(self):
        cars_created = + 1
        car = Petrol()
        if not cars_created % 3:
            car = Diesel()
        if not cars_created % 5:
            car.tank = 75
            return car


class Car(object):

    def __init__(self, mileage, price=10000, tank=60):
        self.price = price
        self.mileage = mileage
        self.tank = tank

    def ride(self):
        pass

    def refill(self):
        pass


class Diesel(Car):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.maximum_mileage = 150000
        self.consumption = 6


class Petrol(Car):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.maximum_mileage = 200000
        self.consumption = 8



#def distance(self):
#   return random.randrange(self.min_range, self.max_range)


#car_pool = (Car() for car in range(30))
#for car in car_pool:
#    print(car.__dict__)