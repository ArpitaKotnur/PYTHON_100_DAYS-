#getter -> it invlokes the funtions which is not visible ( visible only inside class)
class myclass:# define a class
    def __init__(self,value):# its a constructor
        self.val=value
    def show(self): # def function
        print(f"value is {self.val}")
    @property # getter type to get the info from the class
    def ten_value(self):
        return 10*self.val
obj=myclass(10) # object of class myclass

print(obj.ten_value) # the value giving 100 cuz it calls the ten_value
obj.show()# actual function call from class
 
# setter -> how to set another value and calling it  or how to permentaly change the value inside class
class dusra_class:
    def __init__(self,value): # again a constructor
        self.real_val=value
    def show_me(self):
        print(f"value is {self.real_val}") # trying to print the real_value
    @property # a getter method to call when required ( kinda function for variable val )
    def two_value(self):
        return 2*self.real_val # returns the manipulated value
    @two_value.setter # sets the new value the the object which was created
    def two_value(self,new_val_to_set):
        self.real_val=new_val_to_set+1 
ocd=dusra_class(10) # object of class dusra_class
ocd.show_me() # initialy shows value 10
ocd.two_value=20 # using setter we set the value as 20
print(ocd.two_value) # now trying to print two_value it will use 21 instead of 10 cuz using setter the value has changed to 20 permentaly 
ocd.show_me() # give 21 cuz now the actual value has changed to 20 and + 1 dues to mentioned in setter
# mostly used for encapsulation

