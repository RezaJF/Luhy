import pymysql as sql
import pandas as pd
import re
import pandas as pd
from pandas import Series,DataFrame

def conn_box():

	db = sql.connect(host="10.20.212.153",user="PremPTS",passwd="123456",db="SNVbox")
	cursor=db.cursor()
	return db,cursor

def conn_var():

	db = sql.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB_new")
	cursor=db.cursor()
	return db,cursor

def get_pos_list():


	tar = "fmd_fmn_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set.tsv"
	data = pd.read_csv(tar,sep='\t')
	data = DataFrame(data)
	pos_list = []
	for index in data["start"]:
		pos_list.append(index)
	return pos_list	

def get_features():
	db,cursor = conn_box()
	q = "SELECT Feature FROM SNVbox.Features;"
	cursor.execute(q)
	Features = cursor.fetchall()
	print(type(Features))
	f_list = []
	for i in Features:
		f_list.append(i[0])
	print(f_list)


def test_db():
	pos_list = get_pos_list()
	print(len(pos_list))
	uid_list = {}
	db,cursor = conn_box()

	for i in pos_list:

		q = "SELECT UID FROM SNVbox.splicetable where pos = '" + str(i) +"';"

		cursor.execute(q)
		uid = cursor.fetchall()
		if uid:

			print(uid)
			uid_list[i] = uid
	print(uid_list)

def get_enst_var():
	tar = "fmd_fmn_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set.tsv"
	data = pd.read_csv(tar,sep='\t')
	data = DataFrame(data)
	db,cursor = conn_var()
	result =pd.DataFrame(columns=('start','aachange','enst','other'))
	for index, row in data.iterrows():
		start = row['start']
		AA = row['aachange']
		q = "SELECT `Accession Number` FROM varientDB.all_info_order where Start = " +str(start) + " and `Mutation AA` like '%" + AA +"';"

		cursor.execute(q)
		enst = cursor.fetchall()
		if enst:
			enst_list = []
			for sample in enst:
				if sample[0] not in enst_list:
					enst_list.append(sample[0])
			if len(enst_list) == 1:
				result = result.append(pd.DataFrame({'start':[start],'aachange':[AA],'enst':[enst_list[0]]}),ignore_index=True)
				print(start,AA,enst_list[0])
			else:
				temp_str = ""
				for j in range(len(enst_list)):
					if j != 0:
						temp_str =temp_str +str(enst_list[j])
				result = result.append(pd.DataFrame({'start':[start],'aachange':[AA],'enst':[enst_list[0]],"other":[temp_str]}),ignore_index=True)
				print(start,AA,enst_list[0],temp_str)
			
		else:
			result = result.append(pd.DataFrame({'start':[start],'aachange':[AA]}),ignore_index=True)
			print(start,AA)

	result.to_csv("get_enst_from_variantDB.csv",index=0)


def get_AA_features():
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	result =pd.DataFrame(columns=('mutation_ref','aachange','Charge','Volume','Hydrophobicity','Grantham','Polarity',\
		'Ex','PAM250','BLOSUM','JM','HGMD2003','VB','Transition','COSMIC','COSMICvsSWISSPROT','HAPMAP','COSMICvsHAPMAP'))




	'''	
	#test

	aachange = 'G474R'
	WildType  = aachange[0]
	Mut = aachange[-1]
	mutation_ref ="test"
	print(Mut)
	q = "SELECT * FROM SNVbox.AA_Features where WildType = '"+ WildType +"' and Mut = '" + Mut +"';"

	cursor.execute(q)
	aa_info = cursor.fetchall()
	print(aa_info)
	result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref],'aachange':[aachange],'Charge':[aa_info[0]['Charge']],'Volume':[aa_info[0]['Volume']],'Hydrophobicity':[aa_info[0]['Hydrophobicity']],'Grantham':[aa_info[0]['Grantham']],'Polarity':[aa_info[0]['Polarity']],'Ex':[aa_info[0]['Ex']],'PAM250':[aa_info[0]['PAM250']],'BLOSUM':[aa_info[0]['BLOSUM']],'JM':[aa_info[0]['JM']],'HGMD2003':[aa_info[0]['HGMD2003']],'VB':[aa_info[0]['VB']],'Transition':[aa_info[0]['Transition']],'COSMIC':[aa_info[0]['COSMIC']],'COSMICvsSWISSPROT':[aa_info[0]['COSMICvsSWISSPROT']],'HAPMAP':[aa_info[0]['HAPMAP']],'COSMICvsHAPMAP':[aa_info[0]['COSMICvsHAPMAP']]}),ignore_index=True)
	print(aachange)
	print(result)

	'''
	
	for index, row in data.iterrows():
		mutation_ref = row['mutation_ref']
		aachange = row['aachange']
		WildType  = aachange[0]
		Mut = aachange[-1]
		q = "SELECT * FROM SNVbox.AA_Features where WildType = '"+ WildType +"' and Mut = '" + Mut +"';"
		cursor.execute(q)
		aa_info = cursor.fetchall()
		result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref],'aachange':[aachange],'Charge':[aa_info[0]['Charge']],'Volume':[aa_info[0]['Volume']],'Hydrophobicity':[aa_info[0]['Hydrophobicity']],'Grantham':[aa_info[0]['Grantham']],'Polarity':[aa_info[0]['Polarity']],'Ex':[aa_info[0]['Ex']],'PAM250':[aa_info[0]['PAM250']],'BLOSUM':[aa_info[0]['BLOSUM']],'JM':[aa_info[0]['JM']],'HGMD2003':[aa_info[0]['HGMD2003']],'VB':[aa_info[0]['VB']],'Transition':[aa_info[0]['Transition']],'COSMIC':[aa_info[0]['COSMIC']],'COSMICvsSWISSPROT':[aa_info[0]['COSMICvsSWISSPROT']],'HAPMAP':[aa_info[0]['HAPMAP']],'COSMICvsHAPMAP':[aa_info[0]['COSMICvsHAPMAP']]}),ignore_index=True)
		print(aachange)


	result.to_csv("get_AA_features_from_SNVBox_fathmm.csv",index=0)

def get_UID():
	miss = 0
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	result =pd.DataFrame(columns=('mutation_ref','transcriptid','enst_snpeff','UID'))	
	for index, row in data.iterrows():
		mutation_ref = row['mutation_ref']
		transcriptid = row['Ensembl_transcriptid']
		enst_snpeff = row['enst_snpeff']
		if not enst_snpeff:
			q = "SELECT * FROM SNVbox.Transcript where EnsT like '" + enst_snpeff +"%';"
		else:
			q = "SELECT * FROM SNVbox.Transcript where EnsT like '" + transcriptid +"%';"
		print(q)
		cursor.execute(q)
		UID = cursor.fetchall()
		try:
			result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref],'transcriptid':[transcriptid],'enst_snpeff':[enst_snpeff],'UID':[UID[0]['UID']]}),ignore_index=True)
		except IndexError:
			result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref],'transcriptid':[transcriptid],'enst_snpeff':[enst_snpeff],'UID':['']}),ignore_index=True)
			miss += 1

				
	result.to_csv("get_UID_from_SNVBox_fathmm.csv",index=0)
	print("miss = ",miss)





def pd_test():
	result =pd.DataFrame(columns=('start','aachange','enst','other'))
	result = result.append(pd.DataFrame({'start':[1],'aachange':[2],'enst':[3]}),ignore_index=True)	
	print(result)
	result.to_csv("test_pd.csv",index=0)
	#test query
	'''
	start = 140453154
	AA = "D594A"
	q = "SELECT `Accession Number` FROM varientDB.all_info_order where Start = " +str(start) + " and `Mutation AA` like '%" + AA +"';"
	print(q)
	cursor.execute(q)
	enst = cursor.fetchall()
	print(enst)	

	'''
def get_Local_Structure_features_by_uid():
	db,cursor = conn_box()
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	result =pd.DataFrame(columns=('UID', 'Pos', 'stab_L', 'stab_M', 'stab_H', 'dssp_E', 'dssp_H', 'dssp_C', 'rsa_B', 'rsa_I', 'rsa_E', 'bfac_S', 'bfac_M', 'bfac_F'))

	cursor = db.cursor(sql.cursors.DictCursor)
	uid_list = data['UID']
	pos_list = data['aachange']
	key_list = ['UID', 'Pos', 'stab_L', 'stab_M', 'stab_H', 'dssp_E', 'dssp_H', 'dssp_C', 'rsa_B', 'rsa_I', 'rsa_E', 'bfac_S', 'bfac_M', 'bfac_F']
	for i in range(len(uid_list)):
		uid = uid_list[i]
		print(uid)
		pos = pos_list[i][1:-1]
		if uid < 100000000:
			q  = "SELECT * FROM SNVbox.Local_Structure where UID = " + str(uid) +" and Pos = " + str(pos) + ";"
			print(q)
			cursor.execute(q)
			re = cursor.fetchall()
			result = result.append(pd.DataFrame({'UID':[re[0]['UID']],'Pos':[re[0]['Pos']],'stab_L':[re[0]['stab_L']],'stab_M':[re[0]['stab_M']],'stab_H':[re[0]['stab_H']],\
				'dssp_E':[re[0]['dssp_E']],'dssp_H':[re[0]['dssp_H']],'dssp_C':[re[0]['dssp_C']],'rsa_B':[re[0]['rsa_B']],'rsa_I':[re[0]['rsa_I']],'rsa_E':[re[0]['rsa_E']],'bfac_S':[re[0]['bfac_S']],\
				'bfac_M':[re[0]['bfac_M']],'bfac_F':[re[0]['bfac_F']]}),ignore_index=True)

		else:
			result = result.append(pd.DataFrame({'UID':[uid],'Pos':[pos],'stab_L':[''],'stab_M':[''],'stab_H':[''],'dssp_E':[''],'dssp_H':[''],'dssp_C':[''],\
				'rsa_B':[''],'rsa_I':[''],'rsa_E':[''],'bfac_S':[''],'bfac_M':[''],'bfac_F':['']}),ignore_index=True)

	result.to_csv("fathmm_local_structure_info.csv",index=0)






	#q = "SELECT * FROM SNVbox.Local_Structure where UID = 77756 and Pos = 474;"
	cursor.execute(q)
	re = cursor.fetchall()	
	print(re[0].keys())

def get_exon_features_by_uid():
	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	uid_list = data['UID']
	exon_list = data['Exon_Rank']
	key_list2 = ['UID', 'Exon', 'Cons', 'snp_den', 'hapmap_snp_den', 'uniprot_den']
	result =pd.DataFrame(columns=('UID', 'Exon', 'Cons', 'snp_den', 'hapmap_snp_den', 'uniprot_den'))
	'''
	q = "SELECT * FROM SNVbox.Exon_Features where UID = 33850 and Exon = 3;"
	cursor.execute(q)
	re = cursor.fetchall()
	print(re[0].keys())
	'''
	for i in range(len(uid_list)):
		uid = uid_list[i]
		#print(uid)
		exon = exon_list[i]
		if uid < 10000000000 and exon < 10000:
			q  = "SELECT * FROM SNVbox.Exon_Features where UID = " + str(uid) +" and Exon = " + str(exon) + ";"
			print(q)
			cursor.execute(q)
			re = cursor.fetchall()
			try:
				result = result.append(pd.DataFrame({'UID':[re[0]['UID']],'Exon':[re[0]['Exon']],'Cons':[re[0]['Cons']],'snp_den':[re[0]['snp_den']],'hapmap_snp_den':[re[0]['hapmap_snp_den']],'uniprot_den':[re[0]['uniprot_den']]}),ignore_index=True)
			except IndexError:
				result = result.append(pd.DataFrame({'UID':[uid],'Exon':[exon],'Cons':[''],'snp_den':[''],'hapmap_snp_den':[''],'uniprot_den':['']}),ignore_index=True)

		else:
			result = result.append(pd.DataFrame({'UID':[uid],'Exon':[exon],'Cons':[''],'snp_den':[''],'hapmap_snp_den':[''],'uniprot_den':['']}),ignore_index=True)

	result.to_csv("fathmm_exon_features_info.csv",index=0)

def get_msa_features_by_uid():
	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	uid_list = data['UID']
	pos_list = data['aachange']
	key_list3 = ['UID', 'Pos', 'Entropy', 'Rel_Entropy', 'num_aligned_species', 'PHC_A', 'PHC_C', 'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', 'PHC_H', 'PHC_I', \
	'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N', 'PHC_P', 'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', 'PHC_squaresum']
	result =pd.DataFrame(columns=(['UID', 'Pos', 'Entropy', 'Rel_Entropy', 'num_aligned_species', 'PHC_A', 'PHC_C', 'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', \
		'PHC_H', 'PHC_I', 'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N', 'PHC_P', 'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', 'PHC_squaresum']))
	'''
	q = "SELECT * FROM SNVbox.Genomic_MSA where UID = 33850 and pos = 3;"
	cursor.execute(q)
	re = cursor.fetchall()
	print(re[0].keys())
	'''
	for i in range(len(uid_list)):
		uid = uid_list[i]
		#print(uid)
		pos = pos_list[i][1:-1]
		if uid < 100000000:
			q  = "SELECT * FROM SNVbox.Genomic_MSA where UID = " + str(uid) +" and Pos = " + str(pos) + ";"
			print(q)
			cursor.execute(q)
			re = cursor.fetchall()
			result = result.append(pd.DataFrame({'UID':[re[0]['UID']],'Pos':[re[0]['Pos']],'Entropy':[re[0]['Entropy']],'Rel_Entropy':[re[0]['Rel_Entropy']],'num_aligned_species':[re[0]['num_aligned_species']],\
				'PHC_A':[re[0]['PHC_A']],'PHC_C':[re[0]['PHC_C']],'PHC_D':[re[0]['PHC_D']],'PHC_E':[re[0]['PHC_E']],'PHC_F':[re[0]['PHC_F']],'PHC_G':[re[0]['PHC_G']],'PHC_H':[re[0]['PHC_H']],'PHC_I':[re[0]['PHC_I']],\
				'PHC_K':[re[0]['PHC_K']],'PHC_L':[re[0]['PHC_L']],'PHC_M':[re[0]['PHC_M']],'PHC_N':[re[0]['PHC_N']],'PHC_P':[re[0]['PHC_P']],'PHC_Q':[re[0]['PHC_Q']],'PHC_R':[re[0]['PHC_R']],'PHC_S':[re[0]['PHC_S']],\
				'PHC_T':[re[0]['PHC_T']],'PHC_V':[re[0]['PHC_V']],'PHC_W':[re[0]['PHC_W']],'PHC_Y':[re[0]['PHC_Y']],'PHC_sum':[re[0]['PHC_sum']],'PHC_squaresum':[re[0]['PHC_squaresum']]}),ignore_index=True)

		else:
			result = result.append(pd.DataFrame({'UID':[uid],'Pos':[pos],'Entropy':[''],'Rel_Entropy':[''],'num_aligned_species':[''],'PHC_A':[''],'PHC_C':[''],'PHC_D':[''],'PHC_E':[''],'PHC_F':[''],'PHC_G':[''],'PHC_H':[''],'PHC_I':[''],'PHC_K':[''],\
				'PHC_L':[''],'PHC_M':[''],'PHC_N':[''],'PHC_P':[''],'PHC_Q':[''],'PHC_R':[''],'PHC_S':[''],\
				'PHC_T':[''],'PHC_V':[''],'PHC_W':[''],'PHC_Y':[''],'PHC_sum':[''],'PHC_squaresum':['']}),ignore_index=True)

	result.to_csv("fathmm_msa_info.csv",index=0)

def get_Regional_Comp_features_by_uid():

	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	uid_list = data['UID']
	pos_list = data['aachange']
	key_list4 = ['UID', 'Pos', 'WildType', 'compP', 'compC', 'compG', 'compDE', 'compQ', 'compH', 'compKR', 'compWYF', 'compILVM', 'entropy', 'normentropy', 'debug']
	result =pd.DataFrame(columns=(key_list4))
	'''
	q = "SELECT * FROM SNVbox.Regional_Comp where UID = 33850 and pos = 3;"
	cursor.execute(q)
	re = cursor.fetchall()
	print(re[0].keys())
	'''
	for i in range(len(uid_list)):
		uid = uid_list[i]
		#print(uid)
		pos = pos_list[i][1:-1]
		if uid < 100000000:
			q  = "SELECT * FROM SNVbox.Regional_Comp where UID = " + str(uid) +" and Pos = " + str(pos) + ";"
			print(q)
			cursor.execute(q)
			re = cursor.fetchall()
			result = result.append(pd.DataFrame({'UID':[re[0]['UID']],'Pos':[re[0]['Pos']],'WildType':[re[0]['WildType']],'compP':[re[0]['compP']],'compC':[re[0]['compC']],'compG':[re[0]['compG']],'compDE':[re[0]['compDE']],'compQ':[re[0]['compQ']],'compH':[re[0]['compH']],'compKR':[re[0]['compKR']],\
				'compWYF':[re[0]['compWYF']],'compILVM':[re[0]['compILVM']],'entropy':[re[0]['entropy']],'normentropy':[re[0]['normentropy']],'debug':[re[0]['debug']]}),ignore_index=True)

		else:
			result = result.append(pd.DataFrame({'UID':[uid],'Pos':[pos],'WildType':[''],'compP':[''],'compC':[''],'compG':[''],'compDE':[''],\
				'compQ':[''],'compH':[''],'compKR':[''],'compWYF':[''],'compILVM':[''],'entropy':[''],'normentropy':[''],'debug':['']}),ignore_index=True)

	result.to_csv("fathmm_Regional_Comp_info.csv",index=0)

def get_Regional_Sam_MSA_by_uid():
	db,cursor = conn_box()
	cursor = db.cursor(sql.cursors.DictCursor)
	tar = "fathmm_snpeff_allinfo.csv"
	data = pd.read_csv(tar)
	data = DataFrame(data)
	uid_list = data['UID']
	pos_list = data['aachange']		

	key_list5 = ['UID', 'Pos', 'Entropy', 'Rel_Entropy', 'PHC_A', 'PHC_C', 'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', 'PHC_H', 'PHC_I', 'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N', 'PHC_P', \
	'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', 'PHC_squaresum']
	key_list5_rename = []
	for j in key_list5:
		key_list5_rename.append('Regional_Sam_' + j)
	print(key_list5_rename)


	result =pd.DataFrame(columns=(key_list5_rename))
	'''
	q = "SELECT * FROM SNVbox.Sam_MSA where UID = 33850 and pos = 3;"
	cursor.execute(q)
	re = cursor.fetchall()
	print(re[0].keys())
	print(key_list5)
	'''
	for i in range(len(uid_list)):
		uid = uid_list[i]
		#print(uid)
		pos = pos_list[i][1:-1]
		if uid < 100000000:
			q  = "SELECT * FROM SNVbox.Sam_MSA where UID = " + str(uid) +" and Pos = " + str(pos) + ";"
			print(q)
			cursor.execute(q)
			re = cursor.fetchall()
			try:
				result = result.append(pd.DataFrame({'Regional_Sam_UID':[re[0]['UID']],'Regional_Sam_Pos':[re[0]['Pos']],'Regional_Sam_Entropy':[re[0]['Entropy']],\
					'Regional_Sam_Rel_Entropy':[re[0]['Rel_Entropy']],'Regional_Sam_PHC_A':[re[0]['PHC_A']],'Regional_Sam_PHC_C':[re[0]['PHC_C']],'Regional_Sam_PHC_D':[re[0]['PHC_D']],'Regional_Sam_PHC_E':[re[0]['PHC_E']],\
					'Regional_Sam_PHC_F':[re[0]['PHC_F']],'Regional_Sam_PHC_G':[re[0]['PHC_G']],'Regional_Sam_PHC_H':[re[0]['PHC_H']],'Regional_Sam_PHC_I':[re[0]['PHC_I']],'Regional_Sam_PHC_K':[re[0]['PHC_K']],\
					'Regional_Sam_PHC_L':[re[0]['PHC_L']],'Regional_Sam_PHC_M':[re[0]['PHC_M']],'Regional_Sam_PHC_N':[re[0]['PHC_N']],'Regional_Sam_PHC_P':[re[0]['PHC_P']],'Regional_Sam_PHC_Q':[re[0]['PHC_Q']],\
					'Regional_Sam_PHC_R':[re[0]['PHC_R']],'Regional_Sam_PHC_S':[re[0]['PHC_S']],'Regional_Sam_PHC_T':[re[0]['PHC_T']],'Regional_Sam_PHC_V':[re[0]['PHC_V']],'Regional_Sam_PHC_W':[re[0]['PHC_W']],\
					'Regional_Sam_PHC_Y':[re[0]['PHC_Y']],'Regional_Sam_PHC_sum':[re[0]['PHC_sum']],'Regional_Sam_PHC_squaresum':[re[0]['PHC_squaresum']]}),ignore_index=True)
			except IndexError:
				result = result.append(pd.DataFrame({'Regional_Sam_UID':[uid],'Regional_Sam_Pos':[pos],'Regional_Sam_Entropy':[''],'Regional_Sam_Rel_Entropy':[''],\
				'Regional_Sam_PHC_A':[''],'Regional_Sam_PHC_C':[''],'Regional_Sam_PHC_D':[''],'Regional_Sam_PHC_E':[''],'Regional_Sam_PHC_F':[''],'Regional_Sam_PHC_G':[''],\
				'Regional_Sam_PHC_H':[''],'Regional_Sam_PHC_I':[''],'Regional_Sam_PHC_K':[''],'Regional_Sam_PHC_L':[''],'Regional_Sam_PHC_M':[''],'Regional_Sam_PHC_N':[''],'Regional_Sam_PHC_P':[''],'Regional_Sam_PHC_Q':[''],\
				'Regional_Sam_PHC_R':[''],'Regional_Sam_PHC_S':[''],'Regional_Sam_PHC_T':[''],'Regional_Sam_PHC_V':[''],'Regional_Sam_PHC_W':[''],'Regional_Sam_PHC_Y':[''],'Regional_Sam_PHC_sum':[''],\
				'Regional_Sam_PHC_squaresum':['']}),ignore_index=True)


		else:
			result = result.append(pd.DataFrame({'Regional_Sam_UID':[''],'Regional_Sam_Pos':[pos],'Regional_Sam_Entropy':[''],'Regional_Sam_Rel_Entropy':[''],\
				'Regional_Sam_PHC_A':[''],'Regional_Sam_PHC_C':[''],'Regional_Sam_PHC_D':[''],'Regional_Sam_PHC_E':[''],'Regional_Sam_PHC_F':[''],'Regional_Sam_PHC_G':[''],\
				'Regional_Sam_PHC_H':[''],'Regional_Sam_PHC_I':[''],'Regional_Sam_PHC_K':[''],'Regional_Sam_PHC_L':[''],'Regional_Sam_PHC_M':[''],'Regional_Sam_PHC_N':[''],'Regional_Sam_PHC_P':[''],'Regional_Sam_PHC_Q':[''],\
				'Regional_Sam_PHC_R':[''],'Regional_Sam_PHC_S':[''],'Regional_Sam_PHC_T':[''],'Regional_Sam_PHC_V':[''],'Regional_Sam_PHC_W':[''],'Regional_Sam_PHC_Y':[''],'Regional_Sam_PHC_sum':[''],\
				'Regional_Sam_PHC_squaresum':['']}),ignore_index=True)


	result.to_csv("fathmm_Regional_Sam_MSA_info.csv",index=0)



if __name__ == "__main__":
	#get_features()
	f_list = ['AABLOSUM', 'AACharge', 'AACOSMIC', 'AACOSMICvsHapMap', 'AACOSMICvsSWISSPROT', 'AAEx', 'AAGrantham', 'AAHapMap', 'AAHGMD2003', 'AAHydrophobicity', 'AAMJ', 'AAPAM250', 'AAPolarity', \
	'AATransition', 'AATripletFirstDiffProb', 'AATripletFirstProbMut', 'AATripletFirstProbWild', 'AATripletSecondDiffProb', 'AATripletSecondProbMut', 'AATripletSecondProbWild', 'AATripletThirdDiffProb', \
	'AATripletThirdProbMut', 'AATripletThirdProbWild', 'AAVB', 'AAVolume', 'AlaSubPHC', 'Altlen', 'ExonConservation', 'ExonHapMapSnpDensity', 'ExonSnpDensity', 'HMMEntropy', 'HMMPHC', 'HMMRelEntropy', 'InsiderPPI',\
	 'MGAEntropy', 'MGAPHC', 'MGARelEntropy', 'NumAlignedSpecies', 'PredBFactorF', 'PredBFactorM', 'PredBFactorS', 'PredRSAB', 'PredRSAE', 'PredRSAI', 'PredSSC', 'PredSSE', 'PredSSH', 'PredStabilityH', 'PredStabilityL', \
	 'PredStabilityM', 'PubMed', 'Reflen', 'RegCompC', 'RegCompDE', 'RegCompEntropy', 'RegCompG', 'RegCompH', 'RegCompILVM', 'RegCompKR', 'RegCompNormEntropy', 'RegCompP', 'RegCompQ', 'RegCompWYF', 'Remaining', 'Transcripts', \
	 'UniprotACTSITE', 'UniprotBINDING', 'UniprotCABIND', 'UniprotCARBOHYD', 'UniprotCOMPBIAS', 'UniprotDensity', 'UniprotDISULFID', 'UniprotDNABIND', 'UniprotDOM_Chrom', 'UniprotDOM_LOC', 'UniprotDOM_MMBRBD', \
	 'UniprotDOM_PostModEnz', 'UniprotDOM_PostModRec', 'UniprotDOM_PPI', 'UniprotDOM_RNABD', 'UniprotDOM_TF', 'UniprotLIPID', 'UniprotMETAL', 'UniprotMODRES', 'UniprotMOTIF', 'UniprotNPBIND', 'UniprotPROPEP', \
	 'UniprotREGIONS', 'UniprotREP', 'UniprotSECYS', 'UniprotSIGNAL', 'UniprotSITE', 'UniprotTRANSMEM', 'UniprotZNFINGER']

	temp_feature_list = ['enst_snpeff', 'transcriptid', 'Exon_Rank', 'Exon_length', 'HGVS.c', 'cDNA.pos', 'cDNA.length', 'CDS.pos', 'CDS.length', 'AA.pos', 'AA.length', 'UID', 'compP', 'compC', 'compG', 'compDE', 'compQ', 'compH', \
	'compKR', 'compWYF', 'compILVM', 'entropy', 'normentropy', 'MSA_Entropy', 'Rel_Entropy', 'num_aligned_species', 'PHC_A', 'PHC_C', 'PHC_D', 'PHC_E', 'PHC_F', 'PHC_G', 'PHC_H', 'PHC_I', 'PHC_K', 'PHC_L', 'PHC_M', 'PHC_N', 'PHC_P', \
	'PHC_Q', 'PHC_R', 'PHC_S', 'PHC_T', 'PHC_V', 'PHC_W', 'PHC_Y', 'PHC_sum', 'PHC_squaresum', 'stab_L', 'stab_M', 'stab_H', 'dssp_E', 'dssp_H', 'dssp_C', 'rsa_B', 'rsa_I', 'rsa_E', 'bfac_S', 'bfac_M', 'bfac_F', 'Charge', 'Volume',\
	 'Hydrophobicity', 'Grantham', 'Polarity', 'Ex', 'PAM250', 'BLOSUM', 'JM', 'HGMD2003', 'VB', 'Transition', 'COSMIC', 'COSMICvsSWISSPROT', 'HAPMAP', 'COSMICvsHAPMAP', 'gene', 'chr', 'start', 'ref', 'alt', 'aachange', 'mutationtype', \
	 'y', 'mutation_ref', 'index', 'SIFT_score', 'SIFT_pred', 'Polyphen2_HDIV_score', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_score', 'Polyphen2_HVAR_pred', 'LRT_score', 'LRT_pred', 'LRT_Omega', 'MutationTaster_score', \
	 'MutationTaster_pred', 'MutationAssessor_score', 'MutationAssessor_pred', 'FATHMM_score', 'FATHMM_pred', 'PROVEAN_score', 'PROVEAN_pred', 'VEST3_score', 'MetaSVM_score', 'MetaSVM_pred', 'MetaLR_score', 'MetaLR_pred', \
	 'M-CAP_score', 'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MutPred_LABEL', 'CADD_phred', 'CADD_LABEL', 'DANN_score', 'fathmm-MKL_coding_score', 'fathmm-MKL_coding_pred', 'Eigen-raw', 'Eigen-PC-raw', 'GenoCanyon_score', \
	 'GenoCanyon_LABEL', 'integrated_fitCons_score', 'GM12878_fitCons_score', 'H1-hESC_fitCons_score', 'HUVEC_fitCons_score', 'GERP++_RS', 'phyloP100way_vertebrate', 'phyloP20way_mammalian', 'phastCons100way_vertebrate', \
	 'phastCons20way_mammalian', 'SiPhy_29way_logOdds', 'CONDEL', 'CONDEL_LABEL', 'CanDrA_Score', 'CanDrA_Category', 'FATHMM_Cancer_score', 'FATHMM_Cancer_pred', 'ParsSNP', 'CHASMplus', 'LRT_score_new', 'MutationTaster_score_new', \
	 'CGC', 'frequency', 'label', 'index1']
	#pd_test()
	#get_UID()
	#get_Regional_Sam_MSA_by_uid()
	#get_UID()

	#get_Local_Structure_features_by_uid()
	#get_exon_features_by_uid()
	#get_msa_features_by_uid()
	#get_Regional_Comp_features_by_uid()
	get_Regional_Sam_MSA_by_uid()



