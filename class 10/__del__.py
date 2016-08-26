class Car:
    def __init__(self, name, color='white'):
        self.color = color
        self.name = name
        print ('Car {} created...'.format(self.name))

    def __del__(self):
        print ('Car {} hana...'.format(self.name))

    def __repr__(self):
        print '{}'.format(self.name)

mazda = Car('mazda')
buick = Car('buick')

