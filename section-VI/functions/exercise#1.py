def myfunc(*args):
    # print(args)
    final_list = []
    for i in args:
        if (i%2==0):
            final_list.append(i)
    # print(final_list)
    return final_list

# myfunc(1,2,3,4,5,6,7,8,9,10)
# ------------------------------


def myfunc2(string):
    fin_string = ""
    
    for i in range(len(string)):
        if i % 2 == 0:
            fin_string = fin_string + string[i].lower() 
        else:
            fin_string = fin_string + string[i].upper()
    print(fin_string)
    return fin_string
        
myfunc2('Anthropomorphism')

