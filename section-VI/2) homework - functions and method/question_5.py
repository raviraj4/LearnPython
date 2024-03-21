# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

my_list = [1,2,3,4,5,6,7,8,9,12,13,14,15,16,15,146,75,35,75,33,32,641,76]
def multiply(lst):
    mult_res = 1
    for i in lst:
        mult_res = i * mult_res
    
    return mult_res

print(multiply(my_list))
        
    