import MySQLdb
import pandas as pd

methods = ['accession_id','SIFT_score','Polyphen2_HDIV_score','Polyphen2_HVAR_score','LRT_score','MutationTaster_score','MutationAssessor_score','FATHMM_score','GERP++_RS',
  'PROVEAN_score','VEST3_score','MetaSVM_score','MetaLR_score','M-CAP_score','REVEL_score','MutPred_score','CADD_phred','DANN_score','fathmm-MKL_coding_score',
  'Eigen-raw','Eigen-PC-raw','GenoCanyon_score','FATHMM_Cancer_score','CHASMplus','CanDrA_Score','ParsSNP','CONDEL','SiPhy_29way_logOdds','integrated_fitCons_score',
  'GM12878_fitCons_score','H1-hESC_fitCons_score','HUVEC_fitCons_score','phyloP100way_vertebrate','phyloP20way_mammalian','phastCons100way_vertebrate','phastCons20way_mammalian']

conn = MySQLdb.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB_new")
cursor=conn.cursor()

s = "SELECT `accession_id`,`position_asc_id`,`position_desc_id`,`gene_symbol_id`,`site_id`,`histology_id` from all_info_order_by_gene_symbol;"
cursor.execute(s)
d = cursor.fetchall()
accession_id = []
position_asc_id = []
position_desc_id = []
gene_symbol_id = []
site_id = []
histology_id = []
for x in d:
	accession_id.append(x[0])
	position_asc_id.append(x[1])
	position_desc_id.append(x[2])
	gene_symbol_id.append(x[3])
	site_id.append(x[4])
	histology_id.append(x[5])
ids = []
ids.append(accession_id)
ids.append(position_asc_id)
ids.append(position_desc_id)
ids.append(gene_symbol_id)
ids.append(site_id)
ids.append(histology_id)

me = []
for x in methods:
	sql = "SELECT accession_id,CASE WHEN @prevRank = `%s` THEN @curRank WHEN @prevRank := `%s` THEN @curRank := @curRank + 1 END AS rank FROM all_info_order_by_gene_symbol, (SELECT @curRank :=0, @prevRank := NULL) r ORDER BY `%s`;"%(x,x,x)
	cursor.execute(sql)
	data=cursor.fetchall()
	tempMethodData = []
	for y in data:
		tempMethodData.append(y[1])
	uniqueSize = str(len(set(tempMethodData)))
	expression = {}
	for y in data:
		expression[y[0]] = str(y[1])+"/"+uniqueSize
	me.append(expression)
conn.close()

res = []
for x in ids[0]:
	temp = []
	for y in me[1:]:
		if x in y:
			temp.append(y[x])
		else:
			temp.append(None)
	res.append(temp)

result = pd.DataFrame(res)
result = pd.concat([pd.DataFrame(ids).T,result],axis=1)
result.to_csv('rankForGene.tsv',sep='\t',header=False,index=False)
