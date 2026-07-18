name="arpita"
for naam in name:
    print(naam)
shop=["apple","banana","orange","kiwi"]
for fruit in shop:
    print(fruit)
    for i in fruit:#nested for loop
        print(i)
for s in range(5):#prints 5-1 till 4
    print(s)
print("-----------------------------------------------")
for t in range(2,9):#from 2 to 9-1 till 8
    print(t)
print("----------------------------------------------")
for t in range(2,11,2):# 2 = startinng 11=till 10 2= step of 2
    print(t)
----------------------------------------------------------------------
i=0
while(i<5):
    print(i)
    i=i+1
c=int(input("enter the value more than 50\n"))
while(c>50):
    c=int(input("enter the value more than 50"))
    print(c)
else:
    print("invalid input") #if while doesn't work then else will
#python doesn't have do while loop as c nd c++ have
# create do while in python by making it infinte loop
while True:
    c=int(input("enter the value more than 50"))
    if(c<50):
        print("invalid input")
        break
