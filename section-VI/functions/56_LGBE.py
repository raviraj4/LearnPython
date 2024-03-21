# local example
# lambda num: num**2
# num is local to this lambda expression

# global example

# GLOBAL
name = "I am global"
def greet():
    # ENCLOSING
    name = "I am enclosing"
    def hello():
        global name
        # LOCAL 
        name = "I am Local"  
        print("hello "+name)
        
    hello()
greet()

print(name)