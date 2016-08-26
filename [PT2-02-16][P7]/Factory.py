class Factory(object):
    cars_created = 0
    def __init__(self, engine='petrol', price=10000, tank=60):
        Factory.cars_created += 1
        self.engine = engine
        self.tank = tank
        self.price = price
        if not Factory.cars_created % 3:
            self.engine = 'diesel'
        if not Factory.cars_created % 5:
            self.tank = 75

print(Factory.cars_created)
print(mazda.__dict__)
print(mazda2.__dict__)
print(mazda3.__dict__)
print(mazda4.__dict__)
print(mazda5.__dict__)




class Car(object):
    def __init__(self,  color, doors, wheels=4):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.tank = 90
        self.engine = None

    def drive(self):
        print('Driving far....')

    def stop(self):
        print('Pushing the brakes!')

    @property
    def fill_tank(self):
        return self.tank

    @fill_tank.setter
    def fill_tank(self, new_value):
        if new_value > self.tank:
            print 'Take to service and replace to bigger'
        self.tank = new_value

    def ride(self):
        self.doors = 'Closed'
        print "Doors closed"

class Van(Car):
    def __init__(self, wheels, weight):
        super(self.__class__, self).__init__()
        self.weight = weight
        self.wheels = wheels

<<<<<<< HEAD:Factory.py
mazda.fill_tank = 100
print (mazda.fill_tank)
mazda.tank = 1000
=======
    @classmethod
    def get_heavy_van(cls):
        pass
>>>>>>> origin/master:Class.py
