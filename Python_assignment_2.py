#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_two(num1,num2):
    total = num1 + num2
    return total

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
print(add_two(number_1, number_2))


# In[2]:


def mul_two(num1, num2):
    mult = (num1 * num2)
    return mult

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
print(mul_two(number_1, number_2))


# In[5]:


def average(numbers):
    average = (sum(numbers)/len(numbers))
    if (average > 90) :
        return "A-grade"
    elif(average >= 75):
        return "B-grade"
    elif(average >= 50):
        return "C-grade"
    elif(average >= 35):
        return "D-grade"
    else:
        return "Fail"
    
print(average([77, 33, 45, 55, 68]))


# In[23]:


def decor(avg):
    def grade(marks):
        average = sum(marks)/len(marks)
        if (average > 90) :
            print ("A-grade")
        elif(average >= 75):
            print ("B-grade")
        elif(average >= 50):
            print ("C-grade")
        elif(average >= 35):
            print ("D-grade")
        else:
            print ("Fail")
        avg(marks)
        
    return grade
@decor
def average_marks(marks):
    total = 0
    no_of_subjects = 0
    for i in marks:
        total = total + i
        no_of_subjects = no_of_subjects + 1
        average = (total/no_of_subjects)
    print("")
    print(f"The total marks of the student are {total} in total no of subjects {no_of_subjects} and the average is {average}")
average_marks([12, 85, 96, 52, 56])



# In[ ]:




