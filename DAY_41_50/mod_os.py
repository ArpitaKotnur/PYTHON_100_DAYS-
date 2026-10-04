import os
if(not os.path.exists("data")):# if folder is not there make it
    os.mkdir("data")# makes a directory
for i in range(0,100):
    os.mkdir(f"data/day{i+1}")
