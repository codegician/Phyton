import os
def rename_files():
    #(1) get files names from a folder
    file_list = os.listdir("/Users/rejoice/Downloads/Phyton/prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/rejoice/Downloads/Phyton/prank")
    #(2) for each files, rename filenames
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_files()
