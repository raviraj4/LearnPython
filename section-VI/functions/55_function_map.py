#  first we need to define a function simple or complex.
def storecalc(price):
    if price >=100:
        return price, 'DISCOUNT'
    else:
        return price, 'sorry, no discount'

mylist = [120,23,10,400,100,99]
for price in map(storecalc,mylist):
    print(price)

# to get in list format 

print(list(map(storecalc,mylist)))



