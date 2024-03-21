# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
st_upd = st.split(" ")
print(st_upd)
for alpha in st_upd:
    print(alpha[0])

# SUCCESS
# >>> 

# C
# a
# l
# o
# t
# f
# l
# o
# e
# w
# i
# t
# s