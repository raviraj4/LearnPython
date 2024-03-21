from collections import Counter
from collections import defaultdict

# counter 
MyList = {1,1,1,2,2,2,2,2,2,3,3,3}
# print(Counter(MyList))

# dict
anime = defaultdict(lambda: "bocha tuza")
anime['deathnote'] = 'lame as fuck'
# print(anime['opm'])

from collections import namedtuple
langs = namedtuple('langs', ['name', 'creator', 'popularity', 'extension'])
cpp = langs(name='c++', creator='Bjarne Stroustrup', popularity='peak',extension='.cpp')
python = langs(name='python', creator='Guido Van Rossum', popularity='peak-lg', extension='.py')
total_langs = {'code123': cpp , 'code546': python}
print(Counter.keys(total_langs))
