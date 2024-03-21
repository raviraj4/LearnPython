#   EXAMPLE 01 >>> for loops
var_list = ['ravi', 'sashi', 'agni', 'karna', 'arjun']
for name in var_list:
    if name == 'karna':
        print(name, ",you are selected!")
    elif name == 'sashi':
        print(name, ",you are almost there. try again later!")
    else:
        print(name, ",you have not been selected!")
