#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Betaine (glyb) reactions

# EC Number 1.2.1.8 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=BADH-RXN
def betaine_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites and reactions
    M_betald = model.metabolites.get_by_id("betald_c")
    M_nad = model.metabolites.get_by_id("nad_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")
    M_glyb = model.metabolites.get_by_id("glyb_c")
    M_nadh = model.metabolites.get_by_id("nadh_c")
    M_h = model.metabolites.get_by_id("h_c")

    R_BETALDHx = Reaction("BETALDHx")
    R_BETALDHx.name = "Betaine Aldehyde dehydrogenase"
    R_BETALDHx.add_metabolites(
        {
            M_betald: -1.0,
            M_nad: -1.0,
            M_h2o: -1.0,
            M_glyb: 1.0,
            M_nadh: 1.0,
            M_h: 2.0
        }
    )

    # EC number 1.1.99.1 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=CHD-RXN

    M_chol = model.metabolites.get_by_id("chol_c")


    chd_rxn = Reaction("CHD-RXN")
    chd_rxn.name = "Choline dehydrogenase"
    chd_rxn.add_metabolites(
        {
            M_chol: -1.0,
            M_betald: 1.0,
            M_h: 2.0
        }
    )

    # There is no explaination for the synthesis of choline 
    # THIS PART MIGHT BE WRONG
    model.add_reactions([R_BETALDHx, chd_rxn])
    return model

