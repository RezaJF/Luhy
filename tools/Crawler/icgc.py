import requests

import json

def catch(project):
	targetlist = ['id', 'icgcId', 'primarySite', 'name', 'tumourType', 'tumourSubtype', 'pubmedIds', 'primaryCountries', 'ssmTestedDonorCount', 'cnsmTestedDonorCount', \
	'stsmTestedDonorCount', 'sgvTestedDonorCount', 'methSeqTestedDonorCount', 'methArrayTestedDonorCount', 'expSeqTestedDonorCount',\
 	'expArrayTestedDonorCount', 'pexpTestedDonorCount', 'mirnaSeqTestedDonorCount', 'jcnTestedDonorCount', 'totalDonorCount', 'totalLiveDonorCount', 'state']

	url="https://dcc.icgc.org/api/v1/projects/"
	url = url + project
	r = requests.get(url)
	t = json.loads(r.text)
	f1 = open("D:/project_info.txt",'a')
	'''
	for i in  targetlist:
		f1.write(i)
		f1.write(",")
	f1.write("\n")
	'''
	for i in  targetlist:
		#print(t[i])
		try:
			f1.write(str(t[i]))
			
		except(KeyError):
			f1.write("null")
		f1.write("=")

	f1.write("\n")
	f1.close()
def new():
	targetlist = ['id', 'icgcId', 'primarySite', 'name', 'tumourType', 'tumourSubtype', 'pubmedIds', 'primaryCountries', 'ssmTestedDonorCount', 'cnsmTestedDonorCount', \
	'stsmTestedDonorCount', 'sgvTestedDonorCount', 'methSeqTestedDonorCount', 'methArrayTestedDonorCount', 'expSeqTestedDonorCount',\
 	'expArrayTestedDonorCount', 'pexpTestedDonorCount', 'mirnaSeqTestedDonorCount', 'jcnTestedDonorCount', 'totalDonorCount', 'totalLiveDonorCount', 'state']

	f2 = open("D:/project_info.txt",'w')
	for i in targetlist:
		f2.write(i)
		f2.write("=")
	f2.write("\n")
	f2.close()



	

info ="D:/d/ICGC_cancer_info.txt"

project ="WT-US"

f = open("D:/d/ICGC_cancer_info.csv",'r')

l = f.readline()

l = f.readline()
while l:
	project = l.split(",")[0]
	print(project)
	catch(project)


	l = f.readline()

#new()






#catch(project)


