# Python Object Oriented Programming - Basics

# When you dont know class contents & avoid compilation error
class EmployeePlaceholder:
    pass


class Employee:
    # Class Constructor, self is similar to instance
    # self points to instance of class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # Self is passed implicitly to every class method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Krupesh', 'Anadkat', 50000)
# Call method through instance
# instance is implicitly passed as argument for self
print(emp1.fullname())

# Call method through Class
# Required to manually pass instance for self parameter
print(Employee.fullname(emp1))
