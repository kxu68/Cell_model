#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# gluconolactone
# g15lac reactions
def gluconolactone_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_glc__D = model.metabolites.get_by_id("glc__D_c")
    M_nad = model.metabolites.get_by_id("nad_c")
    M_nadh = model.metabolites.get_by_id("nadh_c")
    M_g15lac = Metabolite(
        "g15lac_c",
        formula="C6H10O6",
        name="D-glucono-1,5-lactone",
        compartment="c"
    )
    M_h = model.metabolites.get_by_id("h_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_g15lac: 0.00346666666666667

        }
    )
    
    R_G1Dx = Reaction("G1Dx")
    R_G1Dx.name = "Glucose 1 dehydrogenase NAD"
    R_G1Dx.add_metabolites(
        {
            M_glc__D: -1.0,
            M_nad: -1.0,
            M_g15lac: 1.0,
            M_h: 1.0,
            M_nadh: 1.0
        }
    )

    model.add_reactions([R_G1Dx])
    return model

