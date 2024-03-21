game_list = [0,1,2]

# display function to display the list

def display_game(game_list):
    print("here is the current list: ")
    print(game_list)

# position choice function to 
def position_choice():
    choice = "wrong"
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ["0","1","2"]:
            print("Sorry! invalid choice")

    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input('type a string to place at position: ')
    game_list[position] = user_placement
    return game_list

def game_choice():
    choice = "wrong"
    while choice not in ['Y','N']:
        choice = input("Do you still want to continue? (Y or N): ")
        if choice not in ["Y","N"]:
            print("Sorry! invalid choice")

    if  choice == "Y":
        return True
    else:
        return False
 
game_on = True
# main code 
while game_on:
    display_game(game_list)    
    choice  = position_choice()
    replacement_choice(game_list,choice )
    display_game(game_list)
    game_on = game_choice()