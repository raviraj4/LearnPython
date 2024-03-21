# EXAMPLE 01>>> BREAK, CONTINUE AND PASS

# word = "madagaskar"
# for letters in word:
#     if letters == "a":
#         continue
#     print(letters)

# >>>
# m
# d
# g
# s
# k
# r
# if instead of using continue we use break keyword we get>>

word = "madagaskar"
for letters in word:
    if letters == "a":
        break
    print(letters)

# >>> m
