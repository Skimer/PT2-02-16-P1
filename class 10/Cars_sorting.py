from pprint import pprint as p
from operator import itemgetter
ENG_TYPE_GASOLINE = 'gasoline'
ENG_TYPE_DIESEL = 'diesel'


class Car(object):
    car_pool = []

    def __init__(self, eng_type, cost, mileage):
        self.eng_type = eng_type
        self.cost = cost
        self.mileage = mileage
        Car.car_pool.append(self)

    def __eq__(self, other):
        return self.cost == other.cost

    def __add__(self, other):
        return self.mileage + other.mileage


    def __getitem__(self, item):
        return getattr(self.item)

    def __repr__(self):
        return ', '.join(str(self.__dict__[_])for _ in self.__dict__)

a = Car(ENG_TYPE_DIESEL, 100, 400)
b = Car(ENG_TYPE_DIESEL, 150, 200)
#Car(ENG_TYPE_DIESEL, 180, 100)
#Car(ENG_TYPE_GASOLINE, 200, 1400)
#Car(ENG_TYPE_GASOLINE, 180, 1200)
#Car(ENG_TYPE_GASOLINE, 80, 1200)

#diesels = filter(lambda x: x.eng_type == ENG_TYPE_DIESEL, Car.car_pool)
#s_diesels = sorted(diesels, key=itemgetter('cost', 'mileage'))
#print(s_diesels)

print (a == b)
print (a + b)

