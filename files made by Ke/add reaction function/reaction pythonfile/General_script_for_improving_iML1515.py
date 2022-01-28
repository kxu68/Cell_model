#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cobra
#initial setup for the origin model
# model_origin= cobra.io.read_sbml_model('iML1515.xml')
#introducing functions to addin reactions and metabolites and biomass reaction changes.
#
# from ipynb.fs.full.f1p_reaction_function import f1p_reaction
# from ipynb.fs.full.urocanate_reaction_function import urocanate_reaction
# from ipynb.fs.full.guanidinoacetate_reaction_function import guanidinoacetate_reaction
# from ipynb.fs.full.tyramine_reaction_function import tyramine_reaction
# from ipynb.fs.full.trans_cinnamate_reaction_function import trans_cinnamate_reaction
# from ipynb.fs.full.glucosamine_reaction_function import glucosamine_reaction
# from ipynb.fs.full.myo_inositol_reaction_function import myo_inositol_reaction
# from ipynb.fs.full.CMP_N_acetylneuraminate_reaction_function import CMP_N_acetylneuraminate_reaction
# from ipynb.fs.full.Carnosine_reaction_function import carnosine_reaction
# from ipynb.fs.full.gluconolactone_reaction_function import gluconolactone_reaction
# from ipynb.fs.full.Dimenthylbenzimidazol_reaction_function import dimenthylbenzimidazol_reaction
# #below is the reactions add only to the model not to biomass
# from ipynb.fs.full.Cartinine_reaction_function import cartinine_reaction
# from ipynb.fs.full.Trimethylamine_Noxide_reaction_function import trimethylamine_noxide_reaction
# from ipynb.fs.full.Betaine_reaction_function import betaine_reaction

### for python import change from ipynb.fs.full directly to the py file name(such as f1p_reaction_function)
from f1p_reaction_function import f1p_reaction
from urocanate_reaction_function import urocanate_reaction
from guanidinoacetate_reaction_function import guanidinoacetate_reaction
from tyramine_reaction_function import tyramine_reaction
from trans_cinnamate_reaction_function import trans_cinnamate_reaction
from glucosamine_reaction_function import glucosamine_reaction
from myo_inositol_reaction_function import myo_inositol_reaction
from CMP_N_acetylneuraminate_reaction_function import CMP_N_acetylneuraminate_reaction
from Carnosine_reaction_function import carnosine_reaction
from gluconolactone_reaction_function import gluconolactone_reaction
from Dimenthylbenzimidazol_reaction_function import dimenthylbenzimidazol_reaction
#below is the reactions add only to the model not to biomass
from Cartinine_reaction_function import cartinine_reaction
from Trimethylamine_Noxide_reaction_function import trimethylamine_noxide_reaction
from Betaine_reaction_function import betaine_reaction
model= cobra.io.read_sbml_model('iML1515.xml')


# In[ ]:


#1 reaction import 
f1p= f1p_reaction(model)
f1p


# In[ ]:


#2 reacyion import
urcan=urocanate_reaction(f1p)
urcan


# In[ ]:


#3 reaction import
gudac=guanidinoacetate_reaction(urcan)
gudac


# In[ ]:


#4 reaction import
tym=tyramine_reaction(gudac)
tym


# In[ ]:


#5 reaction import
cinnm=trans_cinnamate_reaction(tym)
cinnm


# In[ ]:


#6 reaction import
gam=glucosamine_reaction(cinnm)
gam


# In[ ]:


#7 reaction import
inost=myo_inositol_reaction(gam)
inost


# In[ ]:


#8 import
cmpacna=CMP_N_acetylneuraminate_reaction(inost)
cmpacna


# In[ ]:


#9 import
carn=carnosine_reaction(cmpacna)
carn


# In[ ]:


#10 import
g15lac=gluconolactone_reaction(carn)
g15lac


# In[ ]:


#11 import
dmbzid=dimenthylbenzimidazol_reaction(g15lac)
dmbzid


# In[ ]:


#12 reaction import
#follow is the function for adding reactions only to model not to biomass reaction
crn=cartinine_reaction(dmbzid)
crn


# In[ ]:


#13 reaction import
tmao=trimethylamine_noxide_reaction(crn)
tmao


# In[ ]:


#14 reaction import
glyb=betaine_reaction(tmao)
glyb


# In[ ]:


cobra.io.sbml.write_sbml_model(glyb,'iML1515_improvedbyKe_reaction.xml')

