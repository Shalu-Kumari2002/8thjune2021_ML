#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
    print(i*'*')
    


# In[2]:


for i in range(10):
    print(i*'*')
    if i == 4:
        break 


# In[10]:


for i in range(10):
    if i == 5 or i == 8:
        continue
    print(i*'*')


# In[11]:


for i in range(5,0,-1):

    print(i*"*")


# In[12]:


a = 6
b = 6

for i in range(1,a,1):
    for n in range(1,i+1):
        print(n,end=" ")
    print(end = '\n')
    


# In[13]:


for i in range(1,a,1):
    for n in range(1,i+1):
        print(i,end=" ")
    print(end = '\n')


# In[16]:


c = 10 
for i in range(1,c+1,1):
    for n in range(1,11,1):
        if n == i:
            print("*",end = "")
        elif n == -i:
            print("*", end = "")
        else:
            print(" ", end= " ")
    print(end = "\n")
        


# In[18]:


c = 10 
for i in range(1,c+1,1):
    for n in range(1,11,1):
        if -n == i:
            print("*",end = "")
        elif -n == -i:
            print("*", end = "")
        else:
            print(" ", end= " ")
    print(end = "\n")


# In[6]:


c = 10 
for i in range(1,c+1,1):
    for n in range(-10,0,1):
        if n == -10 or n == -1:
            print("*",end = "\n")
        else
        
    print(end = '\n')
       


# In[ ]:





# In[ ]:




