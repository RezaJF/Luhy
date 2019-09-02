'''
Charge
Volume
Hydrophobicity
Grantham
Polarity
Ex
PAM250
BLOSUM
JM
HGMD2003
VB
Transition
COSMIC
COSMICvsSWISSPROT
HAPMAP
COSMICvsHAPMAP
'''
#'Charge':[aa_info['Charge']],
f = open("a.csv","r")
l =f.readline()
s = ""
s2 =""
key_list = ['UID', 'Pos', 'stab_L', 'stab_M', 'stab_H', 'dssp_E', 'dssp_H', 'dssp_C', 'rsa_B', 'rsa_I', 'rsa_E', 'bfac_S', 'bfac_M', 'bfac_F']
key_list2 = ['UID', 'Exon', 'Cons', 'snp_den', 'hapmap_snp_den', 'uniprot_den']
key_list3 = ['UID', 'Pos', 'Entropy', 'Rel_Entropy', 'num_aligned_species', 'PHC_A', 'PHC_C', 'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', 'PHC_H', 'PHC_I', \
	'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N', 'PHC_P', 'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', 'PHC_squaresum']
key_list4 = ['UID', 'Pos', 'WildType', 'compP', 'compC', 'compG', 'compDE', 'compQ', 'compH', 'compKR', 'compWYF', 'compILVM', 'entropy', 'normentropy', 'debug']
key_list5 = ['acc_num', 'position','descr']
key_list5_rename = ['acc_num', 'position','descr']
for i in key_list5:
	#print(l)
	s = s+"'" + str(i) + "':[re[0]['" + str(i) +"']],"
	s2 = s2+"'" + str(i) + "':[''],"

print(s)
print(s2)

print("#################################")
s = ""
s2 = ""
for i in range(len(key_list5)):
	#print(l)
	s = s+"'" + str(key_list5_rename[i]) + "':[re[0]['" + str(key_list5[i]) +"']],"
	s2 = s2+"'" + str(key_list5_rename[i]) + "':[''],"

print('result = result.append(pd.DataFrame({'+s+'}),ignore_index=True)')
print("#############################")
print('result = result.append(pd.DataFrame({'+s2+'}),ignore_index=True)')
