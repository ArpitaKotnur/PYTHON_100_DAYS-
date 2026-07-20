marks=[3,5,6,"arpiiii",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(len(marks))
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])
if 7 in marks:
    print("yessss")
else:
    print("no")
#list compression
lis=[i*i for i in range(10)]
print(lis)
lis=[i for i in range(10)]
print(lis)
lis=[i for i in range(20) if i%2==0]
print(lis)
#slicing
print(marks[1:7:2])
l=[11,45,1,7,5,9,2]
print(l)
l.append(10)#appends at end
print(l)
l.reverse()#reverse the list
print(l)
l.sort()#sort the list in assending order
print(l)
l.sort(reverse=True)#sort thr list in dessending order
print(l)

print(l.index(1))#whats the index of one
print(l.count(1))#counts the occurence of 1
m=l
m[0]=0
print(l)#m is refernce not new list to make it as new list 
s=l.copy()
s[0]=25
print(l)
print(s)
l.insert(3,555)#inserts at index of 3
#to permanat merge
p=["wow","shit"]
l.extend(p)
print(l)
#for normal merge
v=[111,222,333,444,666]
print(l+v)
