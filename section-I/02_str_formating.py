# string formating
from unittest import result
print('so hello, I am going to {}' .format('Ladak!'))

print("In Ladak I will visit {} {} {}" .format(
    "mountain,", "lakes", "and shops"))

print("{2} is dumb, {0} is really smart and {1} is extraordinary" .format(
    "arnold", "amy", "maimi"))

print('the {b} is black, {c} is white and the {k} is pale!' .format(
    b='bird', c='cat', k='king'))

# below. you can see by mentioning :1.4 we mean 1 whitespace and 4 numbers to display which is --> 1.235
result = 1.234533
print("the result is {r:1.4}" .format(r=result))

# another way of string formating is:
number = 12
name = "pravin"
print(f"hello {name}'s age is {number} ")

print("{p} rules!".format(p="python"))
