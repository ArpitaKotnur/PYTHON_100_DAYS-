#sets= this are collection of unique and well defined object and also unordered
s={7,5,9,5,9,5,7,3,4,3,2}
print(s)
p={}
print(type(p))#cuz dict also have same syntax 
#so to create empty set we use
g=set()
print(type(g))
info={"hiii",2,89.4,False}#yeah more than one data type
for i in info:
    print(i)
#sets cannot be changed once it get that position kinda immutable cuz it is ordered so no indes for set
print(s[2])#will through error
