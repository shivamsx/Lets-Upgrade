#!/usr/bin/env python
# coding: utf-8

# In[45]:


def fabi(num):
    x,y = 0,1
    for i in range(num):
        yield(x**2)
        x,y = y, x+y
total = 0
for j in fabi(4):
    total = total + j
    print(j)
print("*"*80)
print("Sum of squares of numbers in fibonacci series using generator is {} ".format(total))


# In[ ]:




