# decorator to mark greet as a static method.

class Employee:
    language= "python" # This is a class attribute
    salary= 120000
    Osalary= 150000
    
# In static method we dont need "self" method
    @staticmethod
    def greet():
        print("Good Morning")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    

a= Employee()
a.greet()
a.getInfo()