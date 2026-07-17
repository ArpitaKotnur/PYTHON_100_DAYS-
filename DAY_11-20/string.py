#strings are immutable 
#all the function which are applied on that will give return a new string cuz string are immuatble
name="arpita"
big_name='''i can 
write anything
also giving space
next line
this is fun 
'''
#multiline  string
count=0
print(name)
print(big_name)
for char in name:
    count=count+1
print("the length of name is\n",count)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
first="hiii"
second=" beauty"
print(first+second)#concatenation
---------------------------------------------------------------------------------------------------------------------
#slicing in python
name="arpita"
print(name[0:4])#including 0 and excluding 4 (from index 0 to 3)
print(name[:5])#it will consider from 0 only
print(name[0:])
print(name[0:-2])# from 0 to len(name)-2 thats ntg but 4
print(name[-4:-2])# len(name)-4 to leg(name)-2
-----------------------------------------------------------------------------------------------------------------------
a="arpita"
print(a.upper())#the variable is not touched (immuatable) 
b="ANJALI"
print(b.lower())
c="!!!!!!!!!!!!!!!!!!hiiii!!!!!!!!!!!!!!!!!!!!!!!!!"
print(c.rstrip("!")) #will only strip the last part not the inial part
d="hii arpita nice to meet you arPita . how can i help you arpita"
print(d.replace("arpita","anjali"))#will change all the occurance of name mentioned
print(d.split(" "))#split the whole string with space and gives output inform of list
print(d.capitalize())# first letter capital baki sab small
print(a.center(50))#make it at center
print(len(a))
print(len(a.center(50)))
print(d.count("arpita"))#counts how many times does arpita occured in string
print(a.endswith("a"))#boolen type of return function, tells does that string ends with char given
print(a.endswith("t",2,5))#can use slicing then endswith 
print(d.find("arpita"))# return index of first occurance of that word or else -1
print(d.find("alisha"))
#print(d.index("alisha")) will through error good for the case wheree you want erroe rather than index
print(b.isalnum())#through true if its A-Z or a-z or 0-9
f="arpi23\n"
print(f.isalpha())#checks is it only contain A-Z or a-z
print(f.islower())
print(f.isprintable())
g="          "
print(g.isspace())


