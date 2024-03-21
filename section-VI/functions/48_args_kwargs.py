def myfunc(name):
    print("My name is ", name)

# myfunc('Chacha Choudhari')

def is_even(x):
    return x%2==0

res = is_even(129268487452452764725)
# print(res)

# args 
def myfunc2(*args):
    return sum((args))

sumfunc = myfunc2(10,15)
# print(sumfunc)

# kwargs
def find_nemothefish(**kwargs):
    print(kwargs)
    for name in kwargs:
        if name == 'Nemo' :
            print("Found NEMO the fish!")
        else:
            # print("khatam. tata. bye bye. goodbye")
            pass
        
find_nemothefish( Dory='fish', simba='lion', cindrella='human', mufasa='lion', Nemo='fish',)

# kwargs + args 
def japan_food(*args,**kwargs):
    print("In japan, I really wish to eat {} {}".format(args[2], kwargs["meal"]))

japan_food(1,2,3,4,5,6, seafood="sushi", meal="ramen", udon="noodles")



