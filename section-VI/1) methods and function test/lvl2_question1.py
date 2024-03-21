# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

a = [3, 1, 3]
def has_33(n):
    for i in range(0,len(n)):
        for j in range(1,len(n)):
            if((n[i]==3) or (n[j]==3)):
                if(n[i]==n[j]):
                     return True
                else:
                    return False
                     
                 
print(has_33(a))