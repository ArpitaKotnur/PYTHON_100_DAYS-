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
s1={1,2,3,4}
s2={3,4,5}
print(s1.union(s2))#same as your set theory , no repeated values are added
print(s1)#untoched untill you change
print(s2)
s1.update(s2)#permanat change
print(s1)
s3={1,2,3,4,5}
s4={3,4,5,6}
print(s3.intersection(s4))#same set theory
print(s3.symmetric_difference(s4))#intersection chod ke sab kuch
print(s3.difference(s4))#ele uniqic to set 1
s3.intersection_update(s4)#permanaent update
print(s3)
s5={1,2,3}
s6={4,5,6}
print(s5.isdisjoint(s6))#no common ele truuu
print(s1.issuperset(s2))#kya s1 suberset hai s2 ka
print(s2.issubset(s1))#kya s2 subset hai s1 ka
s5.add(567)#parmanent change
print(s5)
s5.discard(89)#will no through error
print(s5)
nikal=s5.pop()#any item will pop out
print(nikal)
print(s5)
del s1#will delete entire set
s2.clear()#will clear entire set
print(s2)

s5.delete(89)#will through error if ele not there
print(s5)








