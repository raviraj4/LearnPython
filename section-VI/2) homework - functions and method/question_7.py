import string 

def ispanagram(str1, alphabet = string.ascii_uppercase):
    set_1 = set((str1.lower().replace(" ","")))
    set_2 = set(string.ascii_lowercase) 

    return set_1.issuperset(set_2)
    
    # return set_1 == set_2                        (alternative way to do it)
    
print(ispanagram("The quick brown fox jumps over the lazy dog"))