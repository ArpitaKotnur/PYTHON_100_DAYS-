# inheritense -> aquiring the propertires from other class and also including your own part 
class employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
    def show_bhai(self):
        print(f"the employee name of employee_id {self.employee_id} is {self.name}")
ob=employee("arpita",12)
ob.show_bhai()
class program(employee): # a class taking propertires from employee
    def greet(self): # must pass self so that all class function can pass
        print(f"hello this is object of class program {self.name}") # can use the propertires or features of inherited class
ject=program("kotnur",750)
ject.greet()
