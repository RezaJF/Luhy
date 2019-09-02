# function: csv ->vcf vcf get enst
import pandas as pd
from pandas import Series,DataFrame

def tf(x):                   #transfrom
	r=-1
	lib1=["Gly","Ala","Val","Leu","Ile","Pro","Phe","Tyr","Trp","Ser","Thr","Cys","Met","Asn","Gln","Asp","Glu","Lys","Arg","His"] 
	lib2=['G','A','V','L','I','P','F','Y','W','S','T','C','M','N','Q','D','E','K','R','H'] 
	for i in range(len(lib1)):
		if lib1[i] == x:
			r=i
	if r>-1:
		return lib2[r]
	else:
		return ''

def change_aa(aa):
	aa = aa[2:]
	#print(aa[0:3])
	ref = tf(aa[0:3])

	alt = tf(aa[-3:])
	pos = str(aa[3:-3])
	return(ref+pos+alt)


def test():
	f = open("test_1.vcf",'r')
	l = f.readline()
	ff = open('all_transcript_id.csv','w')
	fff = open('all_transcript_id_match.csv','w')
	data = pd.read_csv('fmd_fmn_have_all_score_del_chasmplus_fathmmcancer_parssnp_training_set_enst.tsv', sep='\t')
	baseset = DataFrame(data)
	aa_base = baseset['aachange']

	max_len = 0
	temp_len = 0
	index = 0
	miss = 0
	while l:
		work_done = False
		aa_change_list = []
		tar = aa_base[index]
		ann_all = l.split('ANN=')[1]
		#print(ann)
		ann_list = ann_all.split(',')
		for ann in ann_list:
			#print(ann)
			word_list = ann.split('|')
			if word_list[1] == 'missense_variant':
				tran_id = word_list[6]
				aa_change = word_list[10]
				aa_change = change_aa(aa_change)
				ff.write(tran_id)
				ff.write(',')
				ff.write(aa_change)
				ff.write(',')
				temp_len= temp_len + 1
			if aa_change == tar and (not work_done):
				fff.write(tran_id)
				work_done = True
		if not work_done:
			miss+=1
			fff.write('miss')





		ff.write('\n')
		fff.write('\n')
		if temp_len > max_len:
			max_len = temp_len
		temp_len = 0

		l = f.readline()
		index += 1
	print(max_len)
	print(miss)

def get_vcf_input():
	f = open('input_fathmm_cancer_training_debug.vcf','w')
	data = pd.read_csv('fathmm_cancer_training_have_all_score_consistent_tend2.tsv', sep='\t')
	baseset = DataFrame(data)

	mutation_ref = baseset['gDNA']
	#print(ref)
	CHROM = baseset['Chr']
	POS = baseset['Start']
	REF = baseset['Ref']
	ALT = baseset['Alt']
	'''
	for info in mutation_ref:
		#print(i)
		temp = info.split(";")
		CHROM.append(temp[1][3:])
		POS.append(temp[2])
		na = temp[4].split('>')
		REF.append(na[0])
		ALT.append(na[1])

	print(CHROM)
	print(POS)
	print(REF)
	print(ALT)
	'''
	for i in range(len(CHROM)):

		f.write(str(CHROM[i]))
		f.write('	')
		f.write(str(POS[i]))
		f.write('	')
		f.write('.')
		f.write('	')
		f.write(REF[i])
		f.write('	')
		f.write(ALT[i])
		f.write('	')
		f.write('.')
		f.write('	')
		f.write('.')
		f.write('	')
		f.write('.')
		f.write('\n')

def get_all_info():
	f = open("fathmm_snpeff.vcf",'r')
	l = f.readline()
	#ff = open('all_transcript_id.csv','w')
	#ff = open('transcript_id_match_allinfo.csv','w')
	data = pd.read_csv('fathmm_cancer_training_have_all_score_consistent_tend2.tsv', sep='\t')
	baseset = DataFrame(data)
	result =pd.DataFrame(columns=('mutation_ref','aachange','enst_snpeff','Exon_Rank','Exon_length','HGVS.c','cDNA.pos','cDNA.length','CDS.pos','CDS.length','AA.pos','AA.length'))	

	aa_base = baseset['aa_mutation']
	mutation_ref = baseset['gDNA']
	max_len = 0
	temp_len = 0
	index = 0
	miss = 0
	while l:
		work_done = False
		aa_change_list = []
		tar = aa_base[index]
		ann_all = l.split('ANN=')[1]
		#print(ann)
		ann_list = ann_all.split(',')
		for ann in ann_list:
			#print(ann)
			word_list = ann.split('|')
			if word_list[1] == 'missense_variant':
				tran_id = word_list[6]
				aa_change = word_list[10]
				aa_change = change_aa(aa_change)



				temp_len= temp_len + 1
			if aa_change == tar and (not work_done):
				Exon = word_list[8].split('/')
				Exon_No = Exon[0]
				Exon_length = Exon[1]
				cDNA = word_list[11].split('/')
				cDNA_pos = cDNA[0]
				cDNA_length = cDNA[1]
				CDS = word_list[12].split('/')
				CDS_pos = CDS[0]
				CDS_length = CDS[1]
				AA = word_list[13].split('/')
				AA_pos = AA[0]
				AA_length = AA[1]

				result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref[index]],'aachange':[tar],'enst_snpeff':[tran_id],'Exon_Rank':[Exon_No],'Exon_length':[Exon_length],\
					'HGVS.c':[word_list[9]],'cDNA.pos':[cDNA_pos],'cDNA.length':[cDNA_length],'CDS.pos':[CDS_pos],'CDS.length':[CDS_length],'AA.pos':[AA_pos],'AA.length':[AA_length]}),ignore_index=True)

				#Allele | Annotation | Annotation_Impact | Gene_Name | Gene_ID | Feature_Type | Feature_ID | Transcript_BioType | Rank | HGVS.c | HGVS.p | cDNA.pos / cDNA.length | CDS.pos / CDS.length | AA.pos / AA.length | Distance | ERRORS / WARNINGS / INFO
				work_done = True
		if not work_done:
			miss+=1
			result = result.append(pd.DataFrame({'mutation_ref':[mutation_ref[index]],'aachange':[tar],'enst_snpeff':[''],'Exon_Rank':[''],'Exon_length':[''],\
				'HGVS.c':[''],'cDNA.pos':[''],'cDNA.length':[''],'CDS.pos':[''],'CDS.length':[''],'AA.pos':[''],'AA.length':['']}),ignore_index=True)






		if temp_len > max_len:
			max_len = temp_len
		temp_len = 0

		l = f.readline()
		index += 1
	print(max_len)
	print(miss)
	result.to_csv("fathmm_snpeff_allinfo.csv",index=0)




#test()



#print(change_aa('p.Asp594Ala'))


#get_vcf_input()
get_all_info()