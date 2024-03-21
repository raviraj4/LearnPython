def count_primes(num):
    if num < 2:
        return 0
    
    # -------------
    #  2 or greater 
    # -------------
    #  store our prime numbers
    primes = [2]
    # counter going up to input num
    x = 3
    #  x is going through every number upto input number
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
            
    print(primes)
    return len(primes)
    
print(count_primes(100000))