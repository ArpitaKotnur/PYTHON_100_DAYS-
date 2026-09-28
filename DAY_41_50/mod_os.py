import os
if(not os.path.exists("data")):#if not there then create one file named data
    os.mkdir("data")
'''for i in range(0,100):
    os.mkdir(f"data/day{i+1}")#if you want to create a n number of folders then '''
#what if i want to rename all folders , manually its not possible
'''for i in range(0,100):
    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")'''
#want to print on terminal?
o_p=os.listdir("data")
print(o_p)
#can have multiple folders inside folders so each folder loop again


