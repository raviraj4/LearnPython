x = []
x.append([1,2])
y = []
y.extend([1,2])
# differece 
# [[1, 2]] 
#  [1, 2]

y.index(1)
y.insert(1,'inserted')
# [[1, 2]] 
#  [1, 2]
# [1, 'inserted', 2]

y.remove('inserted')
#[1, 2]
y.reverse()
y.sort()
