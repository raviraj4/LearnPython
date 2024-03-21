# dict comprehension
# basic syntax of a dictionary
d = {'k1':1, 'k2':2}

# dict comprehension (not widely used)
a = {x:x**3 for x in range(1,5)}
a1 = {a:b**3 for a,b in zip(['animal','bird'], range(1,5))}
# print(a1)
for k in d.values():
    print(k)
for k in d.items():
    print(k)
for k in d.keys():
    print(k)
