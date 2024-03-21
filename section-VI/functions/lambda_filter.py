# using lambda instead of function...this way we dont need to define the function.
list_o = [1,2,3,4,5,6,7,8]
print(list(filter(lambda num:num%2==0, list_o)))
for num in list(filter(lambda num:num%2==0, list_o)):
    print(num) 