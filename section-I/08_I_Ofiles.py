# from importlib.resources import contents


# my_files = open('myfiles_69.txt')
# print(my_files.read())
# # >>>
# my_files.seek(0)
# content = my_files.readlines()
# print(content)

from re import A


with open('myfiles_69.txt', mode='w') as my_files:
    content = my_files.read()
# when mode='w' error is --> unsupported operation
