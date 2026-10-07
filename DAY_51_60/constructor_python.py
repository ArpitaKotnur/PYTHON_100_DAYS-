class student:
    def __init__(self,name,occ): # its a constructor
        self.name=name # name != name first name is class ka name and second one is parameter
        self.occupation=occ
    def say_your_name(self):
        print(f"{self.name} is a {self.occupation}")
a=student("arpita","product management") # dont give 3 argument because it have self - self is for object itself 
b=student("john snow","night watch") # if you dont pass argument it will give error
a.say_your_name()
b.say_your_name()
