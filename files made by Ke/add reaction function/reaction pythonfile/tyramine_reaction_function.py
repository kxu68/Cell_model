#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Tyramine (Tym) reactions

# EC Number 4.1.1.25 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=TYROSINE-DECARBOXYLASE-RXN
def tyramine_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites
# 
    M_tyr = model.metabolites.get_by_id("tyr__L_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_co2 = model.metabolites.get_by_id("co2_c")
    M_tym = Metabolite(
        "tym_c",
        formula="C8H12NO",
        name="Tyramine",
        compartment="c"
    )
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_tym: 0.0000249972208533333

        }
    )
# add reactions
#
    R_TDC = Reaction("TDC")
    R_TDC.name = "Tyrosine Decarboxylase Reaction"
    R_TDC.add_metabolites(
        {
            M_tyr: -1.0,
            M_h: -1.0,
            M_co2: 1.0,
            M_tym: 1.0
        }
    )

    model.add_reactions([R_TDC])
    return model

