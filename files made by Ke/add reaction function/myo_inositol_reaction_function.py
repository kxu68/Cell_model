#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# myo-inositol reactions
def myo_inositol_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
#     get the existing metabolites or creat new ones in the model
    M_mi3p__D = Metabolite(
        "mi3p__D_c",
        formula="C6H11O9P",
        name="1D-myo-Inositol (3)-phosphate",
        compartment="c"
    )
    M_g6p = model.metabolites.get_by_id("g6p_c")
    M_inost = model.metabolites.get_by_id("inost_c")
    M_pi = model.metabolites.get_by_id("pi_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_inost: 0.0000190666666666667

        }
    )
# add reactions 
    R_mi3ps = Reaction("MI3PS")
    R_mi3ps.name = "Myo Inositol 1 phosphate synthase Reaction"
    R_mi3ps.add_metabolites(
        {
            M_g6p: -1.0,
            M_mi3p__D: 1.0
        }
    )

    R_mi3pp = Reaction("MI3PP")
    R_mi3pp.name = "Myo-inositol 1-phosphate Reaction"
    R_mi3pp.add_metabolites(
        {
            M_h2o: -1.0,
            M_mi3p__D: -1.0,
            M_inost: 1.0,
            M_pi: 1.0
        }
    )


    model.add_reactions(
        [
            R_mi3ps, R_mi3pp
        ]
    )
    return model

