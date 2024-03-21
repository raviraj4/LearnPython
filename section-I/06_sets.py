# sets
var_set = set()
var_set.add(100)
var_set.add(345)
var_set.add(69)
var_set.add(79)
print(var_set)

#  above method is not best practice to add elements to sets! instead
list_01 = [23, 34, 22, 66, 45, 26]
print(set(list_01))
# >>> {34, 66, 45, 22, 23, 26}

# Write an expression that would turn the string 'Mississippi'  into a set of unique letters:
# solution
print(set('Mississippi'))
# >>> {'M', 's', 'i', 'p'}
