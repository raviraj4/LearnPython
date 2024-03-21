# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for temp in range(1,101): 
    if temp%3==0 and temp%5==0:
        print("fizzbuzz")
    elif temp%3==0 and temp%5!=0:
        print("fizz")
    elif temp%5==0 and temp%3!=0:
        print("buzz")
   
    else:
        print(temp)

# FAILED + FAILED + WATCHED SOLN THEN SUCCESS
# >>>  
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16
# 17
# fizz
# 19
# buzz
# fizz
# 22
# 23
# fizz
# buzz
# 26
# fizz
# 28
# 29
# fizzbuzz
# 31
# 32
# fizz
# 34
# buzz
# fizz
# 37
# 38
# fizz
# buzz
# 41
# fizz
# 43
# 44
# fizzbuzz
# 46
# 47
# fizz
# 49
# buzz
# fizz
# 52
# 53
# fizz
# buzz
# 56
# fizz
# 58
# 59
# fizzbuzz
# 61
# 62
# fizz
# 64
# buzz
# fizz
# 67
# 68
# fizz
# buzz
# 71
# fizz
# 73
# 74
# fizzbuzz
# 76
# 77
# fizz
# 79
# buzz
# fizz
# 82
# 83
# fizz
# 97
# 98
# fizz
# buzz
