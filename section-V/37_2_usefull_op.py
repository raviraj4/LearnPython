# zip function >> you can do this to more than two lists
# the zip fuction stores value in some xyz location!
# something like this -->  <zip object at 0x00000204A8F3DEC0>
name_first_list = ["raj","shyam", "mohan", "george"]
name_last_list = ["patil", "prakhar", "bhargav", "benny"]
age_list = [17, 18, 21, 23]
# print(zip(name_first_list,name_last_list,age_list))
for items in zip(name_first_list, name_last_list, age_list):
    print(items)
    
# lets say we added uneven values in list...then what?
# the zip will just ignore the rest of the values!

#  in Keyword >>
print(25 in age_list)
# >>> False
dict = {"key_1": 6969}
print(6969 in dict.values())