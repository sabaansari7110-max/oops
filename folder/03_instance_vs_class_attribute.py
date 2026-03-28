# Instance attribute, take preference over class attribute during assignement and retrival.

class Employee:
    language= "python" # This is a class attribute
    salary= 120000


a= Employee()
a.language=  "java"   # This is a instance attribute
print(a.language, a.salary)