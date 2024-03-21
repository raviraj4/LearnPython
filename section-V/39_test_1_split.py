# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
st_upd = st.split()
for alphas in st_upd:
    if alphas[0]=="s":
        print(alphas)

# SUCCESS 
# >>>
# start
# s
# sentence