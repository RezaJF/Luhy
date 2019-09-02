import MySQLdb
import pandas as pd

f = "id	SIFT_score	SIFT_converted_rankscore	FATHMM_score	FATHMM_converted_rankscore	PROVEAN_score	PROVEAN_converted_rankscore	Polyphen2_HDIV_score	Polyphen2_HDIV_rankscore	Polyphen2_HVAR_score	Polyphen2_HVAR_rankscore	MutationTaster_score	MutationTaster_converted_rankscore	MutationAssessor_score	MutationAssessor_score_rankscore	VEST3_score	VEST3_rankscore	MutPred_score	MutPred_rankscore	LRT_score	LRT_converted_rankscore	LRT_Omega	MetaSVM_score	MetaSVM_rankscore	MetaLR_score	MetaLR_rankscore	Reliability_index	M-CAP_score	M-CAP_rankscore	REVEL_score	REVEL_rankscore	CADD_raw	CADD_raw_rankscore	CADD_phred	DANN_score	DANN_rankscore	fathmm-MKL_coding_score	fathmm-MKL_coding_rankscore	Eigen-raw	Eigen-phred	Eigen-PC-raw	Eigen-PC-phred	Eigen-PC-raw_rankscore	GenoCanyon_score	GenoCanyon_score_rankscore	integrated_fitCons_score	integrated_fitCons_score_rankscore	integrated_confidence_value	GM12878_fitCons_score	GM12878_fitCons_score_rankscore	GM12878_confidence_value	H1-hESC_fitCons_score	H1-hESC_fitCons_score_rankscore	H1-hESC_confidence_value	HUVEC_fitCons_score	HUVEC_fitCons_score_rankscore	HUVEC_confidence_value	GERP++_NR	GERP++_RS	GERP++_RS_rankscore	phyloP100way_vertebrate	phyloP100way_vertebrate_rankscore	phyloP20way_mammalian	phyloP20way_mammalian_rankscore	phastCons100way_vertebrate	phastCons100way_vertebrate_rankscore	phastCons20way_mammalian	phastCons20way_mammalian_rankscore	SiPhy_29way_logOdds	SiPhy_29way_logOdds_rankscore	CHASM_breast_score	CHASM_lung_score	ParsSNP	FATHMM_Cancer_score	CanDrA_Score	CONDEL"
methods = f.split('\t')

conn = MySQLdb.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB")
cursor=conn.cursor()

s = "SELECT `id` from methods;"
cursor.execute(s)
d = cursor.fetchall()
ids = []
for x in d:
	ids.append(x[0])

me = []
for x in methods:
	sql = "SELECT id,CASE WHEN @prevRank = `%s` THEN @curRank WHEN @prevRank := `%s` THEN @curRank := @curRank + 1 END AS rank FROM methods, (SELECT @curRank :=0, @prevRank := NULL) r ORDER BY `%s` DESC;"%(x,x,x)
	cursor.execute(sql)
	data=cursor.fetchall()
	expression = {}
	for y in data:
		expression[y[0]] = y[1]
	me.append(expression)
conn.close()

res = []
for x in ids:
	temp = []
	for y in me[1:len(me)]:
		if y[x]:
			temp.append(str(y[x])[:-2]+"/"+str(len(set(y.values()))))
		else:
			temp.append(None)
	res.append(temp)

result = pd.DataFrame(res)
#result = pd.concat([pd.DataFrame(ids),result],axis=1)
result.to_csv('rankCount.tsv',sep='\t',header=False,index=False)

'''res = pd.DataFrame()
i = 0
for x in methods:
	res[x] = me[i]
	i += 1
print res'''

