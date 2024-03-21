import time
def mainfunc(func):
    def timecal_wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"it took {t1} to complete task {func.__name__}")
    return timecal_wrapper
    
@mainfunc
def do_this():
    time.sleep(1.4)

@mainfunc
def printmenu():
    us_pw_dict  = {'navin': "12",'pritam':"13", 'mahesh':"14", 'minakshi':"15", 'rohit':"16"}

    take_input = input("enter username: ") 
    take_pw = input("enter password: ")
    if take_input in us_pw_dict:
        if us_pw_dict[take_input] == take_pw:
            print(f'login for user: {take_input} successful.')
        else:
            print('invaid username or password try again')
    else:
        print("invalid username")
    time.sleep(.4)

do_this()
printmenu()
print('Done')