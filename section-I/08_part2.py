# WITH THIS CODE I CREATED A TEXT FILE WITHOUT THE HELP OF FILE MANAGER!😈
with open('abcd.txt', mode='w') as f:
    f.write('I WROTE THIS FILE!')
with open('abcd.txt', mode='r') as f:
    print(f.read())
