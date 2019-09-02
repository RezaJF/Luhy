import MySQLdb

fdata = ['id','SIFT_score','Polyphen2_HDIV_score','Polyphen2_HVAR_score','LRT_score','MutationTaster_score','MutationAssessor_score','FATHMM_score','GERP++_RS',
  'PROVEAN_score','VEST3_score','MetaSVM_score','MetaLR_score','M-CAP_score','REVEL_score','MutPred_score','CADD_phred','DANN_score','fathmm-MKL_coding_score',
  'Eigen-raw','Eigen-PC-raw','GenoCanyon_score','FATHMM_Cancer_score','CHASMplus','CanDrA_Score','ParsSNP','CONDEL','SiPhy_29way_logOdds','integrated_fitCons_score',
  'GM12878_fitCons_score','H1-hESC_fitCons_score','HUVEC_fitCons_score','phyloP100way_vertebrate','phyloP20way_mammalian','phastCons100way_vertebrate','phastCons20way_mammalian',
  'CADD_raw']


sql = "CREATE TABLE floatscores (\n"
for x in fdata[0:-1]:
	template = "`%s` DOUBLE,\n"%x
	sql += template
sql += "`%s` DOUBLE\n"%fdata[-1]
sql += ");"
conn = MySQLdb.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB")
cursor=conn.cursor()

cursor.execute(sql)
conn.commit()
conn.close()