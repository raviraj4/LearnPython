mynums = [1,2,3,4,5,6]
print(list(map(lambda num : num**2,mynums)))
for num in list(map(lambda num: num** 2, mynums)):
    print(num)

# using lambda instead of function...this way we dont need to define the function.