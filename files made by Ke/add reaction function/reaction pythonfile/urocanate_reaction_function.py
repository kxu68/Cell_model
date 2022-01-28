#!/usr/bin/env python
# coding: utf-8

# In[2]:


# urocanate reactions
def urocanate_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
#     get the existing metabolites or creat new ones in the model
    M_his__L = model.metabolites.get_by_id('his__L_c')
    M_nh4 = model.metabolites.get_by_id('nh4_c')
    M_urcan = Metabolite(
        'urocanate_c',
        formula = 'C6H5N2O2',
        name = 'urocanate',
        compartment = 'c')
#     add metabolites inside the biomass function
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_urocan: 0.000291950497833333

        }
    )
#     create the reaction  and add metabolites inside
# Unification Links: BRENDA:4.3.1.3, ENZYME:4.3.1.3, IUBMB-ExplorEnz:4.3.1.3
    R_HAL = Reaction('HAL')
    R_HAL.name = 'Histidine Ammonia-lyase Reaction'
    R_HAL.add_metabolites({
        M_his__L: -1.0,
        M_nh4: 1.0,
        M_urcan: 1.0})

    model.add_reactions([R_HAL])
    return model
#     cobra.io.sbml.write_sbml_model(model,'iML1515_urocan_reaction.xml')
    #


# In[3]:


# import cobra
# from cobra import Model, Reaction, Metabolite
# model= cobra.io.read_sbml_model('iML1515.xml')
# urocanate_reaction(model)


# In[ ]:




