#!/usr/bin/env python
# coding: utf-8

# In[27]:


class isnegative (Error):
    pass


# In[31]:


def tempreature(celcius):
    temp_kelvin = celcius + (273.15)
    print (f"The tempreature of {celcius} degree in kelvin is : {temp_kelvin}")
    temp_farenheit = ((celcius * (9/5)) + 32)
    print (f"The tempreature of {celcius} degree in farenheit is : {temp_farenheit}")
    choice = input("Do you want to convert the tempreature from kelvin to farenheit answer in Y/N : ")
    if (choice == "Y"):
        try:
            kelvin = float(input("Enter the tempreature in Kelvin : "))
            
        except ValueError:
            print("Enter only float values")
            
        else:
            farenheit = (((kelvin - 273.15)*9/5)+32)
        try:
            if (farenheit > 0):
                return f"The tempreature of {kelvin} kelvin in farenheit is : {round(farenheit,2)}"
            else:
                raise isnegative
        except isnegative:
            return "Value is negative hence it can not display the result."
                
    else:
        print("")
    
    
try:
    temp = float(input("Enter the temptrature in degree celcius : "))
except ValueError:
    print("Enter only float values")
else:
    print(tempreature(temp))
finally :
    print("*"*65)


# In[26]:


class Error (Exception):
    pass


# In[ ]:




