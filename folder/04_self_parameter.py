# self refers to the instance of the class. It is automatically passed with a function call from the object

class Employee:
    language= "python" # This is a class attribute
    salary= 120000
    Osalary= 150000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    

a= Employee()



a.getInfo()