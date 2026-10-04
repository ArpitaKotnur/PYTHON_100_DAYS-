def square(value):
    return value*value
print(square(2))
# instead of this we can doo this
doub=lambda value: value*value # its a anonymous function( function that doesnt have name)
cube=lambda x: x*x*x # mostly used for passing function as argument or creating a short function
print(doub(4))
print(cube(2))
def addition(fx,value):
    return fx(value)+value
print(addition(lambda x:x*x*x,2))
print(addition(doub,2))


