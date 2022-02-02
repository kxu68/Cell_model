#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cobra

model_ke= cobra.io.read_sbml_model('iML1515_improvedbyKe_reaction.xml')
model_ke


# In[7]:


model_ke.optimize().objective_value


# In[10]:


model_origin= cobra.io.read_sbml_model('iML1515.xml')
model_origin


# In[8]:


model_origin.optimize().objective_value


# In[11]:


model_justin= cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
model_justin


# In[9]:


model_justin.optimize().objective_value


# In[ ]:




