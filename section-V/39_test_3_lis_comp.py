# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

my_list = [*range(1,50)]
for nums in my_list:
    if nums%3==0:
        print(nums)
        
# SUCCESS 
# >>>
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
# 33
# 36
# 39
# 42
# 45
# 48