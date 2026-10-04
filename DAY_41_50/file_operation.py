#reading a file
f=open('first_file.txt','r')
print(f) # variable which contains the information of file
text=f.read()
print(text)
f.close() # best practice to close the file once done with job or else changes won't be changed
#'r' = read mode ( default mode), like that only we have several mode w=removes existing data from file and the new one,
#'a'= appends the data with existing data
# 'x' = create , it create new file and raise error if already exist
#'rt'= read in text mode and this is by default 
# 'b' = reads in binary mode
# writing a file
f=open('first_file.txt','w')
f.write("dekho bachoo its all moha maaya") # whole content will be replaced
f.close()
f=open('first_file.txt','r')
padho=f.read()
print(padho)
f.close()
# appending data
f=open('first_file.txt','a')
f.write(" i want you to focus")
f.close()
f=open('first_file.txt','r')
padho=f.read()
print(padho)
f.close()
# so done with writing f.open and f.close , then we have simple method
with open('first_file.txt','a') as f:
    f.write(" here we go arpii")
with open('first_file.txt','r') as f:    
    nonsence=f.read()
    print(nonsence)
