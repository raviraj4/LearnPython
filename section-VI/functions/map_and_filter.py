num_list = [1,2,3,4,5]

squared = list(map(lambda num: num**2, num_list))

print(squared)

even_squared = list(filter(lambda num: num%2==0, squared))

print(even_squared)

    
    