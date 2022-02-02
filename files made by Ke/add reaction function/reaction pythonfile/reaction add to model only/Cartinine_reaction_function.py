#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# cartinine (crn) reactions

# EC Number 1.14.11.1 https://metacyc.org/META/NEW-IMAGE?type=EC-NUMBER&object=EC-1.14.11.1 
def cartinine_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites and reactions
    M_gbbtc = model.metabolites.get_by_id("gbbtn_c")
    M_akg = model.metabolites.get_by_id("akg_c")
    M_crn = model.metabolites.get_by_id("crn_c")
    M_succ = model.metabolites.get_by_id("succ_c")
    M_co2 = model.metabolites.get_by_id("co2_c")

    R_BTYBTHD = Reaction("BTYBTHD")
    R_BTYBTHD.name = "γ-butyrobetaine dioxygenase"
    R_BTYBTHD.add_metabolites(
        {
            M_gbbtc: -1.0,
            M_akg: -1.0,
            M_crn: 1.0,
            M_succ: 1.0,
            M_co2: 1.0
        }
    )

    # EC Number 1.3.8.13 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=CROBETREDUCT-RXN

    M_bbtcoa = model.metabolites.get_by_id("bbtcoa_c")
    M_nadph = model.metabolites.get_by_id("nadph_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_ctbtcoa = model.metabolites.get_by_id("ctbtcoa_c")

    R_CTBTYCRDT = Reaction("CTBTYCRDT")
    R_CTBTYCRDT.name = "crotonobetainyl-CoA reductase"
    R_CTBTYCRDT.add_metabolites(
        {
            M_bbtcoa: -1.0,
            M_nadph: -1.0,
            M_h: -1.0,
            M_nadph: 1.0,
            M_ctbtcoa: 1.0,
        }
    )

    model.add_reactions([R_BTYBTHD, R_CTBTYCRDT])
    return model

