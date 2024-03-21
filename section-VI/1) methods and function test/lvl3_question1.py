# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(list):
    dummy_list = [0,0,7,'a']
    for num in list:
        if num == dummy_list[0]:
            dummy_list.pop(0)

    return len(dummy_list) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,2,3,4,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
    