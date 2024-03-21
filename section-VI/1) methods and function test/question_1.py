# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(n1,n2):
    if(n1%2 == 0 and n2%2==0):
        if(n1<n2):
            return n1
        else:
            return n2
    elif((n1%2==0 and n2%2!=0) or (n1%2!=0 and n2%2==0) or (n1%2!=0 and n2%2!=0)):
        if(n2<n1):
            return n1
        else:
            return n2
        
print("function 1: (which is a longer code with multiple if else statement)\n")
print(lesser_of_two_evens(2,4)) 
print(lesser_of_two_evens(2,5)) 
    
# shorter code:  
def lesser_of2_even(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
    
print("function 2 (shorter more efficient code)\n")
print(lesser_of2_even(2,4))
print(lesser_of2_even(2,5))
    