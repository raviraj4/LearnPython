# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!
my_string = "Hello Mr. Rogers, how are you this fine Tuesday?"

def case_checker(strings):
    up_count = 0
    low_count = 0
    
    for alphabets in strings:

        if (alphabets.isupper()== True):
            up_count = up_count + 1
        elif alphabets.islower()== True:
            low_count = low_count + 1
        else:
            pass
        
    print(f"original string: {strings}")
    print(f"uppercase characters: {up_count}")
    print(f"lowercase characters: {low_count}", )
             

case_checker(my_string)
