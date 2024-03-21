
from random import shuffle

def shuffle_v2(my_list):
    shuffle(my_list)
    # print(my_list)
    return my_list


 
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        print("-----------------------------------")
        guess = input("Pick a number (0,1 or 2): ")
        print("-----------------------------------")
    
    return int(guess)

# my_index = player_guess()  # function call

# now, we need a function to combine player_guess() and shuffled list
    
def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print("CORRECT GUESS!")
    else:
        print("wrong! try again.")
        print(my_list)


# INITIAL LIST  
my_list = [' ','O',' ']

# SHUFFLE LIST 
mixedup_list = shuffle_v2(my_list) # function call 

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list, guess)