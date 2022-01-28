#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# glucosamine (gam) reactions
# EC Number 3.1.3.- https://metacyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-17745
def glucosamine_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_gam6p = model.metabolites.get_by_id("gam6p_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")
    M_gam = model.metabolites.get_by_id("gam_c")
    M_pi = model.metabolites.get_by_id("pi_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_gam: 0.000137252098233333
        }
    )

    R_PPMEH = Reaction("PPMEH")
    R_PPMEH.name = "Phosphoric Monoester Hydrolases Reaction"
    R_PPMEH.add_metabolites(
        {
            M_gam6p: -1.0,
            M_h2o: -1.0,
            M_gam: 1.0,
            M_pi: 1.0
        }
    )

    model.add_reactions([R_PPMEH])
    return model

