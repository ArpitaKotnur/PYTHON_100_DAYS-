f=open('first_file.txt','r')
i=0
'''while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in math is : {m1}")
    print(f"marks of student {i} in english is : {m2}")
    print(f"marks of student {i} in sst is : {m3}")
    print(line)    '''
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])/2
    m2=int(line.split(",")[1])/2
    m3=int(line.split(",")[2])/2
    print(f"half marks of student {i} in math is : {m1}")
    print(f"half marks of student {i} in english is : {m2}")
    print(f"half marks of student {i} in sst is : {m3}")
    print(line)    
