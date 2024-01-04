import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)# to split file name and extension
    extension = extension[1:] # get rid of the dot
    
    if extension == 'pdf':
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)