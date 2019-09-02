import requests

import json

def getnuiport(acc_id):

	url="http://www.ebi.ac.uk/pdbe/api/mappings/all_isoforms/"
	url = url + acc_id
	r = requests.get(url)
	t = json.loads(r.text)
	print(t)
	uni_list = []
	for i in t[acc_id]['PDB'].keys():
		print(i)	
		uni_list.append(i)
	return uni_list


acc_id = "P83949-6"
l = getnuiport(acc_id)

print(l)
