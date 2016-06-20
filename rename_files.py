import os
import re

def rename_files():
    #(1) get file names from a folder
    files_folder = os.getcwd() + "//prank//"
    print (os.getcwd())
    file_list = os.listdir(files_folder)

    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + re.sub("[0-9]", "", file_name, 0,0))
        os.rename(files_folder  + file_name, files_folder  +  re.sub("[0-9]", "", file_name, 0,0))

    file_list = os.listdir(files_folder )
    print (file_list)
    
rename_files()
