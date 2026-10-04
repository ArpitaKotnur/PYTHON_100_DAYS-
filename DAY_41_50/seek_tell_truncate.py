with open('first_file.txt','r') as f:
    print(type(f))
    f.seek(10)# will directly seek to that position instead of sequentially going like a[10]
    print(f.tell())# will tell where is your current pointer 
    data=f.read(5)
    print(data)
with open('first_file.txt','w') as t:
    t.write("helloo guys ")
    t.truncate(2) # will truncate and keep that much only in file
with open('first_file.txt','r') as padho:
    oodhu=padho.read()
    print(oodhu)
