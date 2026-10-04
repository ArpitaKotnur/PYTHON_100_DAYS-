def cube(x):
    return x*x*x
l=[1,2,3,4,5,6]
newl=[]
#normal way
for i in l:
    newl.append(cube(i)) # lengthy and not used 
print(newl)
#map
cube_list=list(map(cube,l)) # map function is for applying function on each ele of list,tuple or any other
print(cube_list)
# filter
def filter_it(value):
    return value>3
filtered_list=list(filter(filter_it,l)) # mostly used for truee or false value cased 
print(filtered_list)# function filters only true value from returend function\
# reduce
from functools import reduce
def addition(x,y):
    return x+y
print(reduce(addition,l)) # [1+2,3,4,5]=> [3+3,4,5]=>[6+4,5]=>[10+5]=>15



    
