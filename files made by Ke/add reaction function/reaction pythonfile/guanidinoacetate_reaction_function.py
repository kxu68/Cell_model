#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# guanidinoacetate reaction

# EC number 2.1.4.1 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=GLYCINE-AMIDINOTRANSFERASE-RXN
def guanidinoacetate_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_arg__L = model.metabolites.get_by_id("arg__L_c")
    M_gly = model.metabolites.get_by_id("gly_c")
    M_gudac = Metabolite(
        "guanidinoacetate_c",
        formula="C3H7N3O2",
        name="guanidinoacetate",
        compartment="c"
    )
    M_orn = model.metabolites.get_by_id("orn_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_gudac: 0.00001348169698

        }
    )
# add reactions 
# MetaNetX (MNX) Equation: MNXR100312  EC Number: 2.1.4.1
    R_GLYAMDTR = Reaction("GLYAMDTR")
    R_GLYAMDTR.name = "Glycine Amidinotransferase Rxn"
    R_GLYAMDTR.add_metabolites(
        {
            M_arg__L: -1.0,
            M_gly: -1.0,
            M_gudac: 1.0,
            M_orn:1.0
        }
    )
    model.add_reactions([R_GLYAMDTR]
    return model

