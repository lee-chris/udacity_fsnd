'''
Created on Apr 17, 2017

@author: Chris
'''
import os

#
# rename_files
#
# Rename all of the files in the target dir to remove all digits
# 
def rename_files(target_dir):
    
    # get file names from a CreateFolder
    file_list = os.listdir(target_dir)
    print(file_list)    
    
    saved_path = os.getcwd()
    print("Current working directory: " + saved_path)
    
    # change working dir to the target dir
    os.chdir(target_dir)
    
    # for each file, rename the file
    table = str.maketrans(dict.fromkeys("0123456789"))
    for file_name in file_list:
        
        # map all of the digits to empty strings
        new_name = file_name.translate(table)
        
        # rename the file
        print("Renaming " + file_name + " to " + new_name)
        os.rename(file_name, new_name)
        
    os.chdir(saved_path)

rename_files("C:\\Users\\Chris\\prank\\prank")