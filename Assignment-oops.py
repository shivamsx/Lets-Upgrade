#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Person:
    def __init__(self, fname, lname, empid, salary):
        self.firstname = fname
        self.lastname = lname
        self.empid = empid
        self.salary = salary
    def details(self):
        return f"My name is {self.firstname} {self.lastname}, My employee id is {self.empid} and salary is {self.salary}"
    
    def job(self):
        self.job = 'backend developer'
        return f"My name is {self.firstname} {self.lastname} and I am {self.job}."
    
class Employee(Person):
    def data(self, height, weight, designation):
        self.nature = 'Polite'
        self.height = height
        self.weight = weight
        self.designation = designation
        return f"Employee {self.nature} is very {self.nature} his height is {self.height} and his designation is {self.designation}."
    
Sunny = Person('Simmy', 'Singh', 15, 457896)
Johny = Employee('John', 'Michel', 22, 489657)
print(Johny.details())
print(Johny.job())
print(Sunny.details())
print(Sunny.job())
print(Johny.data(180, 90, 'Data analyst'))


# In[ ]:




