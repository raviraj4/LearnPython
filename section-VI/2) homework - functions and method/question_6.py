# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
a_str = "nurses run" #True
b_str = "racecar"   #True
c_str = "unga bunga agnub agnu" # True
d_str = "confused mf" # True


def palindrome(input_str):
    inp_without_spaces = input_str.replace(" ","") # 
    rev = ''.join(reversed(input_str))
    inp_reversed = rev.replace(" ","")

    if(inp_without_spaces == inp_reversed):
        return True
    else:
        return False

print(palindrome(a_str))
print(palindrome(b_str))
print(palindrome(c_str))
print(palindrome(d_str))


        
    
    
    