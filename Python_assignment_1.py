#!/usr/bin/env python
# coding: utf-8

# In[16]:


def largest():
    total = int(input(" Enter the total no of float values : "))
    list_numbers = []
    num = 0
    for i in range(total):
        decimal = float(input("Please enter the float value : "))
        list_numbers.append(decimal)
    print(list_numbers)
    for max in list_numbers: 
        if num < max:
            num = max
    print(num)
largest()


# In[17]:


num_list = [42.36, 99.99, 58.36]

if ((num_list[0] < num_list[1]) and (num_list[1] > num_list[2])):
    print(f'The greatest number is {num_list[1]}')
    
elif ((num_list[0] > num_list[1]) and (num_list[0] > num_list[2])):
    print(f'The greatest number is {num_list[0]}')
    
elif ((num_list[0] < num_list[1]) and (num_list[1] < num_list[2])):
    print(f'The greatest number is {num_list[2]}')

else:
    print("All the numbers are equal")
    


# In[21]:


num_list = [42.36, 99.99, 58.36]
num_list.sort(reverse= True)
print(num_list[0])


# In[26]:


num_list = [42.36, 99.99, 58.36]
new_list = sorted(num_list, reverse= True)
print(new_list[0])


# In[45]:


def ages(Human_age, Dog_age):
    if (Human_age < 0 or Dog_age < 0):
        return ('invalid data')
    
    elif (Human_age == 0 or Dog_age == 0):
        return (f'The age of the dog is {Human_age} ')
    
    elif (Human_age == 1 or Dog_age == 0):
        return (f'The age of the dog is {Human_age} ')
    
    else:
        Human_age = (3*(Dog_age - 1) + 4)
        return (f'If the age of the dog is {Dog_age} & the corresponding age of the human being will be {Human_age}')
    

H_age = int(input("Please enter the age of the human being : "))
D_age = int(input("Please enter the age of the dogs : "))
print("")
print("*" * 70)
print("")
print(ages(H_age, D_age))


# In[ ]:




