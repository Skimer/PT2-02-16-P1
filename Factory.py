class Car(object):
    def __init__(self,  color, doors, wheels=4):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.tank = 90

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

mazda = Car(color='white', doors='open')

mazda.fill_tank = 100
print (mazda.fill_tank)
mazda.tank = 1000