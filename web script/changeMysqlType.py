import MySQLdb

fdata = ['sift_score', 'polyphen2_hvar_score', 'lrt_score', 'mutationassessor_score', 'provean_score', 'vest3_score', 'metalr_score', 'm_cap_score', 'revel_score', 'mutpred_score', 'cadd_raw', 'dann_score', 'eigen_raw', 'chasmplus', 'condel',  'fathmm_cancer_score', 'parssnp', 'candra_score']

conn = MySQLdb.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB")
cursor=conn.cursor()

for x in fdata:
	sql = 'alter table `all_info` modify column %s float(50);'%x
	cursor.execute(sql)
conn.commit()
conn.close()