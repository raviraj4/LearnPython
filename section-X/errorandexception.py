# problem 1 -----------
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print( "cannot use the operator on strings")
    
# problem 2 ------------     
def ask():
    while True:
        try:
            num = int(input("enter number:"))  
        except:
            print("try again")
            continue
        else:    
            False
            break
    
    sqr = num**2    
    print("the square is: ")
    print((sqr))

ask()

