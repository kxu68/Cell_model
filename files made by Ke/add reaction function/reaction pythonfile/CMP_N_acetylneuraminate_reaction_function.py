#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# cmpacna reactions "cmpacna_c": 0.08657083577

# EC number 5.3.1.19 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=L-GLN-FRUCT-6-P-AMINOTRANS-RXN

def CMP_N_acetylneuraminate_reaction(model):
    import cobra
    from cobra import Model, Reaction, Metabolite
#     get the existing metabolites or creat new ones in the model
    M_f6p = model.metabolites.get_by_id("f1p_c")
    M_gln__L = model.metabolites.get_by_id("gln__L_c")
    M_gam6p = model.metabolites.get_by_id("gam6p_c")
    M_glu__L= model.metabolites.get_by_id("glu__L_c")

    R_GF6PTA = Reaction("L-GLN-FRUCT-6-P-AMINOTRANS-RXN")
    R_GF6PTA.name = "L-GLN-FRUCT-6-P-AMINOTRANS-RXN"
    R_GF6PTA.add_metabolites(
        {
            M_f6p: -1.0,
            M_gln__L: -1.0,
            M_gam6p: 1.0,
            M_glu__L:1.0
        }
    )

    # EC number 5.4.2.10 https://biocyc.org/gene?orgid=META&id=EG11553#tab=RXNS

    M_gam6p = model.metabolites.get_by_id("gam6p_c")
    M_gam1p = model.metabolites.get_by_id("gam1p_c")

    R_PGAMT = Reaction("PGAMT")
    R_PGAMT.name = "Phosphoglucosamine mutase"
    R_PGAMT.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I",
    R_PGAMT.add_metabolites(
        {
            M_gam6p:-1.0,
            M_gam1p:1.0
        }
    )

    # EC number 2.3.1.157 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=2.3.1.157-RXN

    M_accoa = model.metabolites.get_by_id("accoa_c")
    M_gam1p = model.metabolites.get_by_id("gam1p_c")
    M_acgam1p = model.metabolites.get_by_id("acgam1p_c")
    M_coa = model.metabolites.get_by_id("coa_c")
    M_h = model.metabolites.get_by_id("h_c")

    R_G1PACT = Reaction("G1PACT")
    R_G1PACT.name = "Glucosamine-1-phosphate N-acetyltransferase"
    R_G1PACT.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I"
    R_G1PACT.add_metabolites(
        {
            M_accoa: -1.0,
            M_gam1p: -1.0,
            M_acgam1p: 1.0,
            M_coa: 1.0,
            M_h: 1.0
        }
    )

    # EC number 2.7.7.23 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=NAG1P-URIDYLTRANS-RXN

    M_utp = model.metabolites.get_by_id("utp_c")
    M_acgam1p = model.metabolites.get_by_id("acgam1p_c")
    M_h = model.metabolites.get_by_id("h_c")
    M_uacgam = model.metabolites.get_by_id("uacgam_c")
    M_ppi = model.metabolites.get_by_id("ppi_c")

    R_UDPACGLP = Reaction("UDPACGLP")
    R_UDPACGLP.name = "UDP N acetylglucosamine diphosphorylase"
    R_UDPACGLP.subsystem = "UDP-N-acetyl-D-glucosamine biosynthesis I"
    R_UDPACGLP.add_metabolites(
        {
            M_utp: -1.0,
            M_acgam1p: -1.0,
            M_h:-1.0,
            M_uacgam: 1.0,
            M_ppi: 1.0
        }
    )

    # EC number 3.2.1.183 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-9987 

    M_uacgam = model.metabolites.get_by_id("uacgam_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")
    M_acmana = model.metabolites.get_by_id("acmana_c")
    M_udp = model.metabolites.get_by_id("udp_c")
    M_h = model.metabolites.get_by_id("h_c")

    R_UAG2EMA = Reaction("UAG2EMA")
    R_UAG2EMA.name = "UDP-N-acetylglucosamine 2-epimerase"
    R_UAG2EMA.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
    R_UAG2EMA.add_metabolites(
        {
            M_uacgam: -1.0,
            M_h2o: -1.0,
            M_acmana: 1.0,
            M_udp: 1.0,
            M_h: 1.0
        }
    )


    # EC number 2.5.1.56 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=N-ACETYLNEURAMINATE-SYNTHASE-RXN

    M_pep = model.metabolites.get_by_id("pep_c")
    M_acmana = model.metabolites.get_by_id("acmana_c")
    M_h2o = model.metabolites.get_by_id("h2o_c")
    M_ncma = Metabolite(
        "ncma_c",
        formula="C11H18NO9",
        name="N-acetyl-β-neuraminate",
        compartment="c"
    )
    M_pi = model.metabolites.get_by_id("pi_c")

    R_ACNPLYS = Reaction("ACNPLYS")
    R_ACNPLYS.name = "N-ACETYLNEURAMINATE SYNTHASE RXN"
    R_ACNPLYS.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
    R_ACNPLYS.add_metabolites(
        {
            M_pep: -1.0,
            M_acmana: -1.0,
            M_h2o: -1.0,
            M_ncma: 1.0,
            M_pi: 1.0
        }
    )



    # EC number 2.7.7.43 https://biocyc.org/META/NEW-IMAGE?type=REACTION&object=RXN-9990

    M_ncma = ncma
    M_ctp = model.metabolites.get_by_id("ctp_c")
    M_cmpacna = Metabolite(
        "cmpacna_c",
        formula="C20H29N4O16P",
        name="CMP-N-acetyl-β-neuraminate",
        compartment="c"
    )
    M_ppi = model.metabolites.get_by_id("ppi_c")

    R_ACNMCT = Reaction("ACNMCT")
    R_ACNMCT.name = "N-acylneuraminate cytidylyltransferase"
    R_ACNMCT.subsystem = "CMP-N-acetylneuraminate biosynthesis II"
    R_ACNMCT.add_metabolites(
        {
            M_ncma: -1.0,
            M_ctp: -1.0,
            M_cmpacna: 1.0,
            M_ppi: 1.0

        }
    )
# add metabolite to biomass    
#     
    R_biomass = model.reactions.get_by_id("BIOMASS_Ec_iML1515_WT_75p37M")
    R_biomass.add_metabolites(
        {
    M_cmpacna: 0.000288569452566667


        }
    )

    model.add_reactions(
        [
            R_GF6PTA, R_PGAMT, R_G1PACT, R_UDPACGLP, R_UAG2EMA, R_ACNPLYS, R_ACNMCT
        ]
    )

    return model

