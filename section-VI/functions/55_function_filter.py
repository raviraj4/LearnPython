def check_even(num):
    return num % 2 == 0 

list_o = [1,2,3,4,5,6,7,8]
print(list(filter(check_even,list_o)))
#  filter -- it filters the list and returns only those items which fulfil the condition.
#  or (iterate through the list.)
for num in list(filter(check_even,list_o)):
    print(num)


