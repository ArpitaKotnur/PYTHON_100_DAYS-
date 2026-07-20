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
