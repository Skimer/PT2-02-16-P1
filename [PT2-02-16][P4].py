myString = "text with syasadfs air mbolsasd a!@#$^&*( ends here"
names = ['train', 'Train', 'Bus', 'Car', 'Airplane', 'Bike', 'Airport']

def symbols(myString):
    new_string = ''
    for letter in myString:
        if letter.isalnum() == True or letter == ' ':
            new_string += letter
        pass
    return new_string

newMyString = symbols(myString)

def mylist(newMyString, names):
    new_list = []
    for letter in newMyString:
        for name in names:
            if name.startswith(letter):
                new_list += name
        return new_list

list = mylist(newMyString, names)
print '', ''.join(list)
