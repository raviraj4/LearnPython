# ----------------------------------------------------
def even_check(n):
    if (n%2==0):
         print(n, "is even")
    else:
        print(n, "is odd")
even_check(100020226252)
# the above solution is good but it can be better
# ----------------------------------------------------
def even(num):
    res = num%2==0
    print(num%2==0)
    return res

even(1)
# the above code does the same thing but it is almost 3 times smaller and more elegant
# ----------------------------------------------------

def check_even_list(num_list):
    # return all the even number
    # empty placeholder
    num_list_upd = []
    for number in num_list:
        if (number%2==0):
            num_list_upd.append(number)
        else:
            pass   # DO NOT RETURN FALSE HERE! its wrong!
    return num_list_upd   # while using return focus on logic not on indentations...

# print(check_even_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))

# >>>
# [2, 4, 6, 8, 10, 12, 14]
# ----------------------------------------------------