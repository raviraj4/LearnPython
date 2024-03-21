# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    res = ''
    for char in text:
        res += char+char+char
    return res
    
print(paper_doll("hello"))
    
def new_func():
    var = input("enter name")