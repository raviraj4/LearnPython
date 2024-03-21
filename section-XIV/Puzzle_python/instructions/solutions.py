# using python os module and regular expression
import os, re, fileinput

# path to the five files
path_c = "D://Computer Science//Courses//Udemy//jose portila-python//python programs//section-XIV//puzzle_python//instructions//extracted_content"

# A function which will take the pattern and path 
def func_finder(patt, path):
    # use the path to find the correct files (one, two, three, four, five)
        for i in os.scandir(path):
            # if i is in the arr(one, two, three, four, five) then we will proceed
            if (i.is_dir()):
            # if (i.is_dir() and i.name in arr_of_filenames): we can add an extra check to make sure we have the desired directory
                for j in os.scandir(i.path):
                    for line in fileinput.input(j.path):
                        searched = re.findall(patt, line)
                        if (searched != []):
                            the_num = "".join(searched) # JUST RETURN SEARCHED IF YOU WANT THE LIST
                            return f"found it! {the_num}"
                            # return searched
    
        # if its a text file we ignore it we don't need to do anything in the else
    
        
pattern1 = r"\d{3}-\d{3}-\d{4}"
# arr1= ['Five', 'Four', 'Three', 'One', 'Two'] => arr_of_filenames=arr1 (pass this as an argument (OPTIONAL))
found = func_finder(patt=pattern1, path=path_c)
print(found)

# output:
# 719-266-2837
# None

# I don't know why I am getting this none value?

    
