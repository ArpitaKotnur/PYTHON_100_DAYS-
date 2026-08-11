d={"hello":"arpita","hello2":"tejaswini"}
print(d["hello"])
d1={42:"chinnu",98:"ananya"}
print(d1[98])
print(d)#will print ordered for bigger version of python
info={'name':'arpita','age':20,'will_vote?':'yes she will'}
print(info['name'])#will through error if the value is  not present
print(info.get('name2'))#will through none if not present
print(info.keys())#will print all the keys
print(info.values())#will print all the values
for i in info:
    print(f"the key value pair are {i} is {info[i]}")#like accessing the index value but not exactly indexing
print(info.items())#will print all the key value pair
for key,value in info.items():
    print(f"the value corresponding {key} is {value}" )#will form 2 different tuple from info.items
#set is unordered and dict is ordered depending on version of python
d.update(d1)
print(d)#permanent update
d.clear()#empty dict you will get
print(d)
emp={}#for empty dict
print(type(emp))
d1.pop(42)#to pop out the value to remove last item popitem(dont pass)
print(d1)
m={1:"arpita",2:"tejaswini",3:"spoorthi"}
del m[2]#will delete key
print(m)
del m #will delete whole dict
print(m)


