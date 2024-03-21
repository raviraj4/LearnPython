import first 

def func2():
    print("func2() in second.py")
 
print("TOP LEVEL in second.py")
first.func1()

if __name__=='__main__':
    print("SECOND.PY being run directly")
    # first.func1()
else:
    print("SECOND.PY is being imported")