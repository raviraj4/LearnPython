# - create files 
# f = open("harekrishna.txt", 'w+')
# f.write("hare krishna hare krishna, krishna krishna hare hare, hare ram hare ram ram ram hare hare"*108)
# f.close()

import os
current_working_directory = os.getcwd() 

# - renaming files: 
# os.rename(src='harekrishna.txt',dst='hareram.txt')

#  - list all directories
game_files = os.listdir("D:\Desktop\Firstgame\Windows")
# print(game_files)

# - moving a file
import shutil
shutil.move("hareram.txt","section-XIV\demo_folder_to_move_text_file")
# print() # it moved the file to desired location

# shutil.rmtree(path) // be carefull using this delete function with no way reverse or undo (MOST DANGEROUS)