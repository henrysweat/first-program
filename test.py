import os
import pandas as pd
import numpy as np

#let the operator know what the current working directory is
begcwd = os.getcwd() 
print(f'Current working directory is: {begcwd}')

#ask the operator which folder they want to work with
print('Please enter the folder name you want to explore:')
folderName = input()

#change cwd to folder requested by operator
os.chdir(str(folderName))

#create cwd filepath object
cwd = os.getcwd()

#create cwd contents object
cwdFolders = os.listdir(cwd)

#remove artificial file from cwd contents
cwdFolders.remove(r'.DS_Store')

#print cwd contents
print(cwdFolders)

#create list to store filepath/filename pairs
fileZip = []
filepathList = []
filenameList = []

#print contents of each folder in cwd contents
for folderName, subfolders, filenames in os.walk(cwd):
    print(f'The folder name is: {folderName}')
    print(f'The subfolders in {folderName} are {subfolders}')
    print(f'The files in {folderName} are {filenames}')
    print()
    for files in filenames:
        filepathList.append(os.path.abspath(files))
        filenameList.append(files)


fileZip = dict(zip(filepathList,filenameList))

df = pd.DataFrame.from_dict(fileZip, orient = 'index')

print(df)

df.to_csv('test.csv')
              
                           
        