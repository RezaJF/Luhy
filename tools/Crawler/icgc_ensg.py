import requests
import json




def catchENSG(ENSG):
	f1 = open("ENSG.txt",'a')
	api ="https://dcc.icgc.org/api/v1/genes/"

	targetlist = ['id', 'symbol', 'name', 'type', 'chromosome', 'start', 'end', 'strand']
	
	#tail ="?include=projects&include=transcripts"

	url = api +ENSG 
	#print(url)
	r = requests.get(url)
	t = json.loads(r.text)
	#print(t.keys())
	#f1.write(r.text)
	for i in targetlist:
		try:
			f1.write(str(t[i]))
		except(KeyError):
			f1.write("null")
		f1.write("=")
	f1.write("\n")
	f1.close()






def new():
	targetlist = ['id', 'symbol', 'name', 'type', 'chromosome', 'start', 'end', 'strand']
	f2 = open("ENSG.txt",'w')

	for i in targetlist:
		f2.write(i)
		f2.write("=")
	f2.write("\n")
	f2.close()


new()

list1 = "icgc_ENSG_info.txt"
f =open(list1,"r")
ENSG = f.readline()
ss = 0
s = 0 
while ENSG:
	if s == 25:
		catchENSG(ENSG[0:-1])
		ENSG =f.readline()
		s = 1
		print(ss,"/20453 ENSG")
		ss = ss + 1
	else:
		catchENSG(ENSG[0:-1])
		ENSG =f.readline()
		s = s + 1
		ss = ss + 1




		
#print(ENSG[0:-1])
#catchENSG(ENSG[0:-1])
#new()