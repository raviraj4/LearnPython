import timeit
import time
def fone(n):
    return [str(nums) for nums in range(n)]

def ftwo(n):
    return list[map(str, range(n) )]

s_time = time.time()
ftwo(100000000)
e_time = time.time()

elap = e_time - s_time
# print(elap)
# b = ftwo(10)
# print(b)

stmt = '''
fone(100)
'''
stmt2 = '''
ftwo(100)
'''
setup = '''
def fone(n):
    return [str(nums) for nums in range(n)]
'''
setup2 = '''
def ftwo(n):
    return list[map(str, range(n) )]
'''
print(timeit.timeit(stmt=stmt, setup=setup, number=100000), ' ', 
timeit.timeit(stmt=stmt2, setup=setup2, number=100000))

