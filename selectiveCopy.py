'''
    Write a program that walks through a folder tree and searches for files with a certain file
    extension (such as .pdf or .jgp). Copy these files from whatever location they are in to a
    new folder.
'''

# import required modules
import os, re, shutil

# create a regex pattern to match the desired result
pattern = re.compile(r'.pdf$|.jpg$', re.I)

# file locations from which to get or put the files
path = 'E:\\autoExperiment'                 # Location of the file from where you want to copy the jpg and pdf files
newPath = 'E:\\newlyOne'                    # Put the location of the folder where you want to copy the jpg and pdf files

# create a for loop to check the condition
for folder, sub, file in os.walk(path):
    # try to match the regex pattern with the file name and copy if matched
    for files in file:
        if pattern.search(files) != None:
            shutil.copy(os.path.join(path, files), newPath)
print('Done')

'''
Note: The path and folder must exist from where you want to copy the files or where you want to copy the files
'''
