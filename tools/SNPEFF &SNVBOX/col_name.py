col_name = ['enst_snpeff', 'transcriptid', 'Exon_Rank', 'Exon_length', 'HGVS.c', 'cDNA.pos', \
            'cDNA.length', 'CDS.pos', 'CDS.length', 'AA.pos', 'AA.length', 'UID', 'compP', 'compC', \
            'compG', 'compDE', 'compQ', 'compH', 'compKR', 'compWYF', 'compILVM', 'entropy',\
            'normentropy', 'MSA_Entropy', 'Rel_Entropy', 'num_aligned_species', 'PHC_A', 'PHC_C', \
            'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', 'PHC_H', 'PHC_I', 'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N',\
            'PHC_P', 'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', \
            'PHC_squaresum', 'stab_L', 'stab_M', 'stab_H', 'dssp_E', 'dssp_H', 'dssp_C', 'rsa_B',\
            'rsa_I', 'rsa_E', 'bfac_S', 'bfac_M', 'bfac_F', 'Charge', 'Volume', 'Hydrophobicity', \
            'Grantham', 'Polarity', 'Ex', 'PAM250', 'BLOSUM', 'JM', 'HGMD2003', 'VB', 'Transition', \
            'COSMIC', 'COSMICvsSWISSPROT', 'HAPMAP', 'COSMICvsHAPMAP', 'gene', 'chr', 'start', 'ref',\
            'alt', 'aachange', 'mutationtype', 'y', 'mutation_ref', 'index', 'SIFT_score', 'SIFT_pred',\
            'Polyphen2_HDIV_score', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_score', 'Polyphen2_HVAR_pred',\
            'LRT_score', 'LRT_pred', 'LRT_Omega', 'MutationTaster_score', 'MutationTaster_pred',\
            'MutationAssessor_score', 'MutationAssessor_pred', 'FATHMM_score', 'FATHMM_pred',\
            'PROVEAN_score', 'PROVEAN_pred', 'VEST3_score', 'MetaSVM_score', 'MetaSVM_pred',\
            'MetaLR_score', 'MetaLR_pred', 'M-CAP_score', 'M-CAP_pred', 'REVEL_score', 'MutPred_score', \
            'MutPred_LABEL', 'CADD_phred', 'CADD_LABEL', 'DANN_score', 'fathmm-MKL_coding_score',\
            'fathmm-MKL_coding_pred', 'Eigen-raw', 'Eigen-PC-raw', 'GenoCanyon_score', \
            'GenoCanyon_LABEL', 'integrated_fitCons_score', 'GM12878_fitCons_score',\
            'H1-hESC_fitCons_score', 'HUVEC_fitCons_score', 'GERP++_RS', 'phyloP100way_vertebrate', \
            'phyloP20way_mammalian', 'phastCons100way_vertebrate', 'phastCons20way_mammalian',\
            'SiPhy_29way_logOdds', 'CONDEL', 'CONDEL_LABEL', 'CanDrA_Score', 'CanDrA_Category',\
            'FATHMM_Cancer_score', 'FATHMM_Cancer_pred', 'ParsSNP', 'CHASMplus', 'LRT_score_new',\
            'MutationTaster_score_new', 'CGC', 'frequency', 'label', 'index1']
new_col = []

for i in col_name:
      if i not in new_col:
            new_col.append(i)
      else:
            print(i)

print(new_col)