import re
msg = "hello the phone number is  91+8900103520 and 91+9000103520"
msg2 = "Hi my phone number is 91+9900123245"

expression = r"91\+\d{10}"

# \d/\D - dig/non-dig, \w/\W - AN/non-AN, \s/\S - blank/non-Blank,  

for match in re.finditer(expression, msg):
    print(match.group()) # group() and groups()
#     8900103520
#     9000103520
    
arr = [msg, msg2]
def find(pattern, arr):
    for match in arr:
        print(re.findall(pattern, match))
        # ['8900103520', '9000103520']
        # ['9900123245']
    
# print(find(expression, arr))
# if we store the re.search(patterm , m) into a variable we can explore the object further, start() and end()

print(re.search('apple|banana', 'I hate banana'))  # or syntax in regex
print(re.findall('..at', 'the bat shat in the hat'))  # wildcard in regex . and ..
print(re.findall('^\d', '2 is not real'))  # checks if the entire sentence starts with a digit (^\d - starts with) (\d$ - ends with)

word = 'this sentence has 1 number in it not 2.'
patt2 = r'[^\d]+'
print(re.findall(pattern=patt2, string=word))

phrase = 'hello! we have a problem. how do we remove the punctaution?'
patt3= r'[^!?.]+' # grouping for exclusion -> [^!?.]
clean = ''.join(re.findall(pattern=patt3, string=phrase))
print(clean)

phrase2 = 'so we have to return hypen-words regaurdless of how long-ish they are'
patt4 = r'[\w]+-[\w]+'
hyphen_only = ' '.join(re.findall(pattern=patt4,string=phrase2))
print(hyphen_only)





    