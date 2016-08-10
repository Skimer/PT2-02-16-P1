someString = 'TEST string'

def to_weird(string):
    new_string = ''
    for i, val in enumerate(string):
        if len(new_string) > 0 and new_string[i - 1].islower() == True:
            new_string = new_string + val.upper()
        else:
            new_string = new_string + val.lower()

    return new_string

print to_weird(someString)


