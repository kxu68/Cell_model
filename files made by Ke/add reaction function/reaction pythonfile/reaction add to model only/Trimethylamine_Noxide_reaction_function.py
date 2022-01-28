#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Trimethylamine N-oxide (tamo) Reactions

# EC Number 1.14.13.148 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-12900
def trimethylamine_noxide_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
# add metabolites and reactions
    M_tma = model.metabolites.get_by_id("tma_c")
    M_nadph = model.metabolites.get_by_id("nadph_c")
    M_o2 = model.metabolites.get_by_id("o2_c")
    M_tmao = model.metabolites.get_by_id("tmao_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")

    R_TMYLMOGN = Reaction("TMYLMON") # Bigg ID for reaction
    R_TMYLMOGN.name = "trimethylamine monooxygenase"
    R_TMYLMOGN.add_metabolites(
        {
            M_tma: -1.0,
            M_nadph: -1.0,
            M_o2: 1.0,
            M_tmao: 1.0,
            M_h2o: 1.0
        }
    )

    # EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-5921

    M_crn = model.metabolites.get_by_id("crn_c")
    M_nadph = model.metabolites.get_by_id("nadph_c")
    M_o2 = model.metabolites.get_by_id("o2_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_msal__L = Metabolite(
        "msal__L_c",
        formula="C4H5O4",
        name="L-malic semialdehyde",
        compartment="c"
    )
    M_tma = model.metabolites.get_by_id("tma_c")
    M_nadp = model.metabolites.get_by_id("nadp_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")

    R_CARNMOGN_rxn_5921 = Reaction("CARNMOGN_rxn_5921")
    R_CARNMOGN_rxn_5921.name = "RXN-5921 carnitine monooxygenase"
    R_CARNMOGN_rxn_5921.add_metabolites(
        {
            M_crn: -1.0,
            M_nadph: -1.0,
            M_o2: -1.0,
            M_h: -1.0,
            M_msal__L: 1.0,
            M_tma: 1.0,
            M_nadp: 1.0,
            M_h2o: 1.0
        }
    )

    # EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-18258

    M_gbbtn = model.metabolites.get_by_id("gbbtn_c")
    M_nadph = model.metabolites.get_by_id("nadph_c")
    M_o2 = model.metabolites.get_by_id("o2_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_sucsal = model.metabolites.get_by_id("sucsal_c")
    M_tma = model.metabolites.get_by_id("tma_c")
    M_nadp = model.metabolites.get_by_id("nadp_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")

    R_CARNMOGN_rxn_18258 = Reaction("CARNMOGN_RXN-18258")
    R_CARNMOGN_rxn_18258.name = "RXN-18258 carnitine monooxygenase UNOFFICIAL"
    R_CARNMOGN_rxn_18258.add_metabolites(
        {
            M_gbbtn: -1.0,
            M_nadph: -1.0,
            M_o2: -1.0,
            M_h: -1.0,
            M_sucsal: 1.0,
            M_tma: 1.0,
            M_nadp: 1.0,
            M_h2o: 1.0
        }
    )

    # EC Number 1.14.13.239 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-18376 

    M_chol = model.metabolites.get_by_id("chol_c")
    M_nadph = model.metabolites.get_by_id("nadph_c")
    M_o2 = model.metabolites.get_by_id("o2_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_gcald = model.metabolites.get_by_id("gcald_c")
    M_tma = model.metabolites.get_by_id("tma_c")
    M_nadp = model.metabolites.get_by_id("nadp_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")

    R_CARNMOGN_rxn_18376 = Reaction("CARNMOGN_RXN-18376")
    R_CARNMOGN_rxn_18376.name = "RXN-18376 carnitine monooxygenase UNOFFICIAL"
    R_CARNMOGN_rxn_18376.add_metabolites(
        {
            M_chol: -1.0,
            M_nadph: -1.0,
            M_o2: -1.0,
            M_h: -1.0,
            M_gcald: 1.0,
            M_tma: 1.0,
            M_nadp: 1.0,
            M_h2o: 1.0
        }
    )


    model.add_reactions([R_TMYLMOGN, R_CARNMOGN_rxn_5921, R_CARNMOGN_rxn_18258, R_CARNMOGN_rxn_18376])
    return model

