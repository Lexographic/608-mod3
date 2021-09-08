#!/usr/bin/env python
# coding: utf-8

# In[7]:


def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
        if value3 > max_value:
            max_value = value3
            return max_value


# In[8]:


maximum(12, 27, 36)


# In[10]:


max(12, 27, 36)


# In[11]:


min(15, 9, 27, 14)


# In[ ]:




