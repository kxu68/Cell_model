#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 5,6-Dimenthylbenzimidazol reactions
def dimenthylbenzimidazol_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites and reactions
    M_fmnh2 = model.metabolites.get_by_id("fmnh2_c")
    M_o2 = model.metabolites.get_by_id("o2_c")

    M_e4p = model.metabolites.get_by_id("e4p_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_dmbzid = model.metabolites.get_by_id("dmbzid_c")

    M_dialurate = Metabolite(
        'dialurate_c',
        formula = 'C4H4N2O4',
        name = 'dialurate',
        compartment = 'c')
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_dmbzid: 00.00000418833775

        }
    )
    

    R_DMBZIDS2_woNAD = Reaction("DMBZIDS2_woNAD")
    R_DMBZIDS2_woNAD.name = "aerobic 5,6-dimethylbenzimidazole synthase"
    R_DMBZIDS2_woNAD.add_metabolites(
            {
            M_fmnh2: -1.0,
            M_o2: -1.0,
            M_h: 1.0,
            M_e4p: 1.0,
            M_dmbzid: 1.0,
            M_dialurate: 1.0
            }
    )


    model.add_reactions([R_DMBZIDS2_woNAD])
    return model

