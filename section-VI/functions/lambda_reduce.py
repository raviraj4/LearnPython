from functools import reduce
list = [1,2,3,4]
print(reduce(lambda x,y:x+y, list))