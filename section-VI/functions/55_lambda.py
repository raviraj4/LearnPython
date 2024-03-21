#  some more examples of lambda

name = ['Ravi', 'Shashi', 'Agni', 'parvati']
print(list(map(lambda b:b[::-1],name)))

# >>> ['ivaR', 'ihsahS', 'ingA', 'itavrap']

for b in list(map(lambda b:b[::-1],name)):
    print(b)
