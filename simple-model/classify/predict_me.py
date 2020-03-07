#!/usr/bin/env python
# coding: utf-8

# In[1]:


from match_my_voice import Model


# In[2]:


us = Model()


# In[3]:


input_str = 'Yesterday, on the eve of #HumanRightsDay, Trump again coddled a dictator—blocking a UN meeting on North Korean human rights, betraying our values. Trump continues to side with the brutal Kim Jong Un regime at the expense of American leadership, our allies, and our security.'


# In[4]:


us.predict(input_str)

