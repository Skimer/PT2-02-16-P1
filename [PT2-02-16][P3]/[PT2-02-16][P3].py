someString = 'TEST string'

def to_weird(string):
    new_string = ''
    for index, letter in enumerate(string):
        if len(new_string) > 0 and new_string[index - 1].islower() == True:
            new_string = new_string + letter.upper()
        else:
            new_string = new_string + letter.lower()

    return new_string

print to_weird(someString)


