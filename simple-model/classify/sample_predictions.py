#!/usr/bin/env python
# coding: utf-8

# In[1]:


from match_my_voice_model import Model


# In[2]:


us = Model()


# In[3]:


input_str = 'No one is born hating another person because of the color of his skin or his background or his religion...'


# In[4]:


us.predict(input_str)

