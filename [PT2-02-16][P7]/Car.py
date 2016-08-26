import random
class Factory(object):
    cars_created = 0

    def __init__(self, engine='petrol', price=10000, tank=60,):

        Factory.cars_created += 1
        self.maximum_mileage = 200000
        self.engine = engine
        self.consumption = 8
        self.tank = tank
        self.price = price
        if not Factory.cars_created % 3:
            self.engine = 'diesel'
            self.consumption = 6
            self.maximum_mileage = 150000
        if not Factory.cars_created % 5:
            self.tank = 75

car_pool = (Factory() for car in range(30))
for car in car_pool:
    print(car.__dict__)


class Route(object):

    def __init__(self, max_range=186000, min_range=29000):
        self.max_range = max_range
        self.min_range = min_range

    @staticmethod
    def distance(self):
        return random.randrange(self.min_range, self.max_range)
distance = Route.distance(Route())
print distance


class Car(Factory):

    def __init__(self, mileage, depreciation,):
        super(self.__class__, self).__init__()
        self.mileage = mileage
        self.depreciation = depreciation

    def fill_tank(self):
        return self.tank









