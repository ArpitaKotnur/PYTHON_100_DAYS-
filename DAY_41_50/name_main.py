def welcome():
    print("hello , namaskara!!! welcome to our channel")
#welcome()
#normally creating like this causes to print or execute all kimd of functions present in that module
#to avoid we use if __name__=="__main__": 
if __name__=="__main__":
    welcome()
#what is __name__ ,its the module itself 
print(__name__)
#the condition means __name__=="__main__", only run when you are the main.py(in the sense when only you are runnig)
