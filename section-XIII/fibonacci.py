# fibonacci without using generators
def fibo_without(n):
    a = 0
    b = 1
    for i in range(n):
        c = a
        a = b
        b = c + b
        print(a)

# fibo_without(10)
    
# fibonacci using generators (MORE EFFECIENT)
def fibo_with(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
        
for i in fibo_with(10):
    print(i)