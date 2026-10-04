import os
folders=os.listdir("data")#will list all the folders in data folder
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
print(os.getcwd())
os.chdir("/path")#will change directory
print(os.getcwd())#displays current working directory
