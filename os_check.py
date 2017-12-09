import os
d = os.getcwd() 
print ("Current directory: ",d)
path =  "F:\\fintech 2016-march2017"
os.chdir(path)
new_d = os.getcwd() 
print ("New directory: ",new_d)
dir_file_list = os.listdir(path)
print (len(dir_file_list))