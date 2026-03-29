# Class "programmer" for storing information of few programmers works at microsoft.

class programmer:
    company= "Microsoft"
    def __init__(self, name, salary,pin):
        self.name= name
        self.salary= salary
        self.pin= pin


p= programmer("Saba" , 120000, 2340081)
print(p.name, p.salary, p.pin, p.company)
