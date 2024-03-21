# tuples are like lists but with parenthesis ()
#      t = ('a', 7.1, 9)
#      t[0] = 'new'
#      print(t)
# Error: 'tuple' object does not support item assignment
# whereas lists allow item assignment
l = [1, 2, 33.45]
print("before:", l)
l[1] = 9
print("after assigning new value:", l)
