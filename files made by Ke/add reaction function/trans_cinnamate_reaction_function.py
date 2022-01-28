#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# trans-Cinnamate (cinnm) reaction

# EC Number 4.3.1.25 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=PHENYLALANINE-AMMONIA-LYASE-RXN
def trans_cinnamate_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_phe__L = model.metabolites.get_by_id("phe__L_c")
    M_cinnm = model.metabolites.get_by_id("cinnm_c")
    M_nh4 = model.metabolites.get_by_id("nh4_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_cinnm: 0.000312863269

        }
    )
#
#
    R_PAL = Reaction("PAL")
    R_PAL.name = "Phenylalanine Ammonia Lyase Reaction"
    R_PAL.add_metabolites(
        {
            M_phe__L: -1.0,
            M_cinnm: 1.0,
            M_nh4: 1.0
        }
    )
    model.add_reactions([R_PAL])
    return model

