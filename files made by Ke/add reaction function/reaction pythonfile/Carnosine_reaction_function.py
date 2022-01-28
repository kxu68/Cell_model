#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Carnosine (carn) reactions
# KEGG ID: C00386
# REACTION NOTE:doi: 10.1111/j.1751-7915.2009.00143.x

# from cobra import Model, Reaction, Metabolite
def carnosine_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_ala_B = model.metabolites.get_by_id("ala_B_c")
    M_his__L = model.metabolites.get_by_id("his__L_c")
    M_atp = model.metabolites.get_by_id("atp_c")
    M_carn = Metabolite(
            "carn_c",
            formula="C9H14N4O3",
            name="carnosine",
            compartment="c"
    )
    M_adp = model.metabolites.get_by_id("adp_c")
    M_pi = model.metabolites.get_by_id("pi_c")
    M_h = model.metabolites.get_by_id("h_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_carn: 0.00002959973967

        }
    )
    
    R_CARNS1 = Reaction("CARNS1")
    R_CARNS1.name = "Carnosine Synthase Reaction"
    R_CARNS1.add_metabolites(
        {
            M_ala_B: -1.0,
            M_his__L: -1.0,
            M_atp: -1.0,
            M_carn: 1.0,
            M_adp: 1.0,
            M_pi: 1.0,
            M_h: 1.0
        }
    )

    model.add_reactions([R_CARNS1])
    return model

