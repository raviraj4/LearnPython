# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_cracker(text):
    words = text.lower().split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False
        
        
print(animal_cracker("RAvi raj"))