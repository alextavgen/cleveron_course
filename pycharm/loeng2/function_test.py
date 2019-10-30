from os import listdir
from os.path import isfile, join

mypath = '/Users/aleksandr.tavgen/Downloads/'

files_list = list()

for filename in listdir(mypath):
    if isfile(mypath + filename):
        files_list.append(filename)

print(files_list)
