def square(number):
    return number**2

my_list = [1,2,3,4]
my_num = 3

# using for loop

# for i in my_list:
#     print(square(i))
    
#  using map function, just using map isn't enough...you've to iterate through it
square_list = []

for item in map(square,my_list):
    square_list.append(item)
    
print(square_list)    
# print(list(map(my_list,my_num)))
