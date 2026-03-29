class Employee():
    language= "java"
    salary= 1200000

    def __init__(self, name, salary, language):
        self.name= name
        self.salary= salary
        self.language= language

        print("Good Moring. Here is the report")

a= Employee("SABA" , 1400000 , "Python")
print(a.name, a.salary, a.language)