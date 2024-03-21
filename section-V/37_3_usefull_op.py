from random import shuffle
# example 1 >>
# random is a built-in library of python.
# shuffle is a function.
list_a = [1,2,3,4,55,22,12]
shuffle(list_a)
print(list_a)
# >>> [22, 2, 4, 3, 55, 1, 12]
print(type(shuffle(list_a)))
# >>> <class 'NoneType'>

from random import randint 
print(randint(1,1000000000))
# >>> 379248048