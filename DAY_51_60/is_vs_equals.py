# is vs ==
# is -> exact location of object in memory 
a=[1,2,3]
b=[1,2,3]
print(a is b) # false-> cuz is treat mutable objects as different
print(a==b) # true-> cuz it compare values not memory
c="arpita"
d="arpita"
print(c is d) # true-> immutable object have same memory location
print(c == d) # true-> compare each and every value 
e=(1,2,3,4)
f=(1,2,3,4)
print(e is f) 
print(e == f)

