

class Employee:
    language= "py" # This is a class attribute
    salary= 120000
    Osalary= 150000


a= Employee()
a.name=  "Saba"   # This is a instance attribute
print(a.name, a.language, a.salary)
                         
olaf= Employee()
olaf.name= "Olaf Elsa"
print(olaf.name, olaf.language, olaf.Osalary)

# Here name is instance attribute and salary and language are classs attributes as they directly belong to the class