# generator functions allow us to write a function that can send back a value and then maybe pick it up where it left off.
def cuber__maker(n):
    # result = []
    for i in range(n):
        yield i**3 # instead of 'result.append(i**3)' now this function becomes a generator
    # return result
    
# for i in cuber__maker(10):
#     print(i)
        
# more efficient

# iter() keyword

name = 'Raj'
name = iter(name)
# print(next(name))
        
# generator comprehension in python
listof_num = [1,2,3,4,5,6]

gencomp = [item for item in listof_num if item < 4]

for o in gencomp:
    print(o)

