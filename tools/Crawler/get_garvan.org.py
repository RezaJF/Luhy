import requests
import json
import pandas as pd
#s = requests.Session()

url_test = "https://vsal.garvan.org.au/ssvs/mgrb/query?chr=2&start=38814&end=46870&limit=10000&sortBy=start&descend=false&skip=0&count=true&annot=true"


wangs_id = "20174221003@stu.suda.edu.cn"
wangs_pwd = "wang1996"

def get_json(chr_number,start,end):
	chr_number = str(chr_number)
	start = str(start)
	end = str(end)
	query = 'https://vsal.garvan.org.au/ssvs/mgrb/query?chr=' + chr_number + '&start=' + start + '&end=' + end + '&limit=10000&sortBy=start&descend=false&skip=0&count=true&annot=true'

	print(query)
	#print(url_test)
	r = requests.get(query,verify = False)
	#print(r.text)
	return json.loads(r.text)


#test 
chr_number = 2
test_start = 38814
test_end = 38815
f = open('hpm_candl_kindriver_gene_mart_export.csv','r')
l =f.readline()
l =f.readline()
print(l)
dict_key = ['v', 'chr', 'start', 'ref', 'alt', 'rsid', 'ac', 'af', 'nHomRef', 'nHet', 'nHomVar', 'type', 'cato', 'eigen', 'sift', 'polyPhen', 'hrcAF', 'gnomadAF', 'gnomadAF_AFR', 'gnomadAF_AMR', \
'gnomadAF_ASJ', 'gnomadAF_EAS', 'gnomadAF_FIN', 'gnomadAF_NFE', 'gnomadAF_OTHD', 'ensemblId', 'consequences', 'geneSymbol', 'clinvar', 'wasSplit']

df =pd.DataFrame(columns=('v', 'chr', 'start', 'ref', 'alt', 'rsid', 'ac', 'af', 'nHomRef', 'nHet', 'nHomVar', 'type', 'cato', 'eigen', 'sift', 'polyPhen', 'hrcAF', 'gnomadAF', 'gnomadAF_AFR', 'gnomadAF_AMR', \
'gnomadAF_ASJ', 'gnomadAF_EAS', 'gnomadAF_FIN', 'gnomadAF_NFE', 'gnomadAF_OTHD', 'ensemblId', 'consequences', 'geneSymbol', 'clinvar', 'wasSplit'))	

while l:
	temp =l.split(",")
	chr_number = temp[0]
	start =temp[1]
	end =temp[2]
	try:
		result = get_json(chr_number,start,end)
		#print(result)
		
		var_list = result['variants']

		for i in var_list:

			df = df.append(pd.DataFrame({'v':[i['v']],'chr':[i['chr']],'start':[i['start']],'ref':[i['ref']],'alt':[i['alt']],'rsid':[i['rsid']],'ac':[i['ac']],'af':[i['af']],'nHomRef':[i['nHomRef']],'nHet':[i['nHet']],'nHomVar':[i['nHomVar']],'type':[i['type']],'cato':[i['cato']],'eigen':[i['eigen']],'sift':[i['sift']],'polyPhen':[i['polyPhen']],'hrcAF':[i['hrcAF']],'gnomadAF':[i['gnomadAF']],'gnomadAF_AFR':[i['gnomadAF_AFR']],'gnomadAF_AMR':[i['gnomadAF_AMR']],'gnomadAF_ASJ':[i['gnomadAF_ASJ']],'gnomadAF_EAS':[i['gnomadAF_EAS']],'gnomadAF_FIN':[i['gnomadAF_FIN']],'gnomadAF_NFE':[i['gnomadAF_NFE']],'gnomadAF_OTHD':[i['gnomadAF_OTHD']],'ensemblId':[i['ensemblId']],'consequences':[i['consequences']],'geneSymbol':[i['geneSymbol']],'clinvar':[i['clinvar']],'wasSplit':[i['wasSplit']],}),ignore_index=True)

	except:
		print('error:chr',chr_number,' : ',start,'-',end)	

	l =f.readline()	
df.to_csv("mgrb_result.csv",index=0)