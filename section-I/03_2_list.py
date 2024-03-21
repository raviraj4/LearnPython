list1 = ['one', 'two', 'three']
print(list1)
list1.append('four')
print(list1)
# output:
# ['one', 'two', 'three']
# ['one', 'two', 'three', 'four']
list1.append('five')
print(list1)
# now,
list1.pop()
print(list1)
# output:    ['one', 'two', 'three', 'four']
list1.pop(0)  # give index in ()
print(list1)
# output :  ['two', 'three', 'four']
list_new = list1.pop(0)
print(list_new)
# output : two
list_test = [1,2,3,4,5,6]
list_test[2] = 100
print(list_test)