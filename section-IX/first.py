# import second

# when we run a py file for instance this one

def func1():
    print('func1() in first.py')

print("TOP LEVEL in first.py")

# python has a bult in variable __name__ which is set to '__main__' as it is the main

if (__name__ == '__main__'):
    print("FIRST.PY is being run directly")
    # second.func2()

else:
    print("FIRST.PY is being imported")
