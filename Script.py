L = '''The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases arent
    special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!'''
print ('Number of letters: ' + str(len(L)))
count = 0
vowels = set('aeiouAOEIU')
for letter in L:
    if letter in vowels:
        count += 1
print ('Number of vowels: ' + str(count))
count = 0
for index in range(0,len(L),1):
    if index == index:
        count =+ 1
    print (str(count) + L[index])










