# reveresing text using ''.join() and iteration 

text = "baba ranchod das"
rev = "".join(reversed(text))

text2 = "hari om tatsav"
rev2 = reversed(text2)

lst = []

for i in rev2:
    lst.append(i)
reversed_text = ''.join(lst)
    
print(rev)
print(reversed_text)

text3 = "homi baba"
replaced_ttx = text3.replace(" ","")
print(replaced_ttx)

text4 = "abcx"
replaced_text4 = text4.replace("x","y")
print(replaced_text4)