
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])
# --> value1
dict1 = {'pen': '10', 'eraser': '5', 'book': '40', 'stapler': '100'}
print(dict1['eraser'])
# --> 5

# you can add lists, dictionaries, float inside a dictionary, for example:

a = {'r1': [22, 33, 23], 'r2': {'n': 'ravi', 'sn': 'mali'}, 'r3': '1.23'}
print(a['r1'])
# >>> [22, 33, 23]
print(a['r1'][1])
# >>> 33
print(a['r2']['n'])
print(a['r2']['sn'])
#  >>>  ravi
#       mali
a['r4'] = 'Jack'
print(a)
# >>> {'r1': [22, 33, 23], 'r2': {'n': 'ravi', 'sn': 'mali'}, 'r3': '1.23', 'r4': 'Jack'}
