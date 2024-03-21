# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low,high+1):
        print(num," is inside the range ", low, "-", high)
    else:
        print(num," is outside the range ", low, "-", high)


def ran_bool(num, low, high):
    if num in range(low,high+1):
        return True
    else:
        return False
        
ran_check(1,5,10)
print(ran_bool(10,5,10))

ran_check(74,5,74)
print(ran_bool(77,5,76))