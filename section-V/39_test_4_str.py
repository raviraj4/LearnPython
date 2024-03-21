# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
sep_line = st.split(" ")
for lets in sep_line :
  if len(lets)%2==0:
      print(lets,"--> is even!")
  elif len(lets)%2!=0:
       print(lets)
  else:
    print(lets)
    
# SUCCESS 
# # >>>

# Print
# every
# word --> is even!
# in --> is even!
# this --> is even!
# sentence --> is even!
# that --> is even!
# has
# an --> is even!
# even --> is even!
# number --> is even!
# of --> is even!
# letters