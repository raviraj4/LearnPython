# ChainMap 
from collections import ChainMap

d1 = {'A':1,'B':2,'C':3}
d2 = {'D':2,'E':2,'F':5}
d3 = {'G':2,'H':3,'I':4}

print(ChainMap(d1,d2,d3))
