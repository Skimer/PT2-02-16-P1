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

    def __del__(self):
        if self.mileage(Petrol) > self.maximum_mileage(Petrol):
            del self
        else:
            self.mileage(Diesel) > self.maximum_mileage(Diesel)
            del self

    def ride(self, distance=random.randrange(29000, 186000)):
        car_distance = self.distance / 1000
        car_consumption = self.distance / 100
        self.mileage = + distance
        self.consumption(Petrol, Diesel) + 0.01 * car_distance
        self.price(Petrol) - 100 * car_distance
        self.price(Diesel) - 120 * car_distance
        self.tank(Petrol) - self.consumption(Petrol) * car_consumption
        self.tank(Diesel) - self.consuption(Diesel) * car_consumption

    @property
    def tank(self):
        return self.tank()

    @tank.setter
    def refill(self):
        if self.tank == 0:
            return self.tank


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


#car_pool = (Car(Diesel, Petrol) for car in range(30))
#for car in car_pool:
#    print(car.__dict__)