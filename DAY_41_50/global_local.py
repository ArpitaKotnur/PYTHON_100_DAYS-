x=5 #global variable
def cute():
    x=3
    print(x)#local variable
print(x)
cute()
#treats both variable different 
#how to change global variable in function
def change_global():
    global x
    x=3
change_global()
print(x)
#dont make mess with using global variable inside function for better programming
