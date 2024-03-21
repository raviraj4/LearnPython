# def display(r1,r2,r3):
#     print(r1)
#     print(r2)
#     print(r3)    
    
# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']
# display(row1,row2,row3)

def users_choice():
    user_inp = 'ThisIsWrong'
    acceptable = range(0,10)
    withinrange = False
    while(user_inp.isdigit()==False or withinrange == False):
        user_inp = input("enter a number in range (1-10): ")
        if (user_inp.isdigit()==False):
            print("sorry. that is not a digit!")

        if user_inp.isdigit()==True:
            if int(user_inp) in acceptable:
                withinrange == True
            else:
                print("sorry this ain't within the range!")
                withinrange == False 
                
    print(int(user_inp))

users_choice()


    