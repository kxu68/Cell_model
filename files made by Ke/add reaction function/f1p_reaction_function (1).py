#!/usr/bin/env python
# coding: utf-8

# In[31]:


# f1p reactions
#change it into function
#does not need to readd biomass reaction
#need to add prefix M/R in the string for the reaction?
#do i also need to import the stuff?
# import cobra
# from cobra import Model, Reaction, Metabolite
# model= cobra.io.read_sbml_model('iML1515.xml')
# globals().clear()
# global model
def f1p_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite 
#     model= cobra.io.read_sbml_model('iML1515.xml')
#     get the existing metabolites or creat new ones in the model
    M_atp = model.metabolites.get_by_id("atp_c")
    M_fru = model.metabolites.get_by_id("fru_c")
    M_adp = model.metabolites.get_by_id("adp_c")
    M_f1p = model.metabolites.get_by_id("f1p_c")
    M_h = model.metabolites.get_by_id("h_c")
    #   crea
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
#     Reaction("BIOMASS_Ec_iML1515_WT_75p37M").add_metabolites(
        {
            M_f1p: 0.000343358096
        }
    )
    
    R_khk = Reaction("KHK")
    R_khk.name = "Ketohexokinase"
    R_khk.add_metabolites(
        {
            M_adp: 1.0,
            M_atp: -1.0,
            M_f1p: 1.0,
            M_fru: -1.0,
            M_h: 1.0
        }
    )
#     Reaction("BIOMASS_Ec_iML1515_WT_75p37M").add_metabolites(
#         {
#             M_f1p: 0.000343358096
#         }
#     )
    model.add_reactions(
        [R_khk]
        )
#     model.repair(rebuild_index=True, rebuild_relationships=True) 
#     cobra.io.sbml.write_sbml_model(model,'iML1515_f1p_reaction.xml')
    return(model)
#     model=cobra.io.read_sbml_model('iML1515_f1p_reaction.xml')
#     cobra.io.save_json_model(model, 'iml1515_f1p_reaction.json')
#     model.optimize().objective_value


# In[32]:


# import cobra
# from cobra import Model, Reaction, Metabolite
# model= cobra.io.read_sbml_model('iML1515.xml')
# xx=f1p_reaction(model)


# In[ ]:





# In[33]:


# f1p=f1p_reaction(model)


# In[34]:


# print(f1p)


# In[ ]:




