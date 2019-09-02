import requests
import json
import pandas as pd
from pandas import Series,DataFrame
import multiprocessing
def get_UUID(row):
	symbol = row[0]
	AA = row[1]
	web_head = "https://portal.gdc.cancer.gov/auth/api/v0/quick_search?query="
	web_tail = "&size=5"
	web_query = web_head + symbol + " " + AA + web_tail

	r = requests.get(web_query)
	t = json.loads(r.text)
	try:
		UUID = t['data']['query']['hits'][0]['ssm_id']
		
	except IndexError:
		UUID = "null"

	return UUID
#main
data = pd.read_csv('tcga_list_debug.csv')
data = DataFrame(data)
length = len(data)
s = 0 
clock = 0
row_list = []

#result =pd.DataFrame(columns=('symbol','aa_mutation','UUID'))
for index,row in data.iterrows():
	symbol = row['symbol']
	AA = row['aa_mutation']
	row_list.append([symbol,AA])
	#UUID = get_UUID(symbol,AA)


cores = multiprocessing.cpu_count()
print(cores)
pool = multiprocessing.Pool(processes=30)
ff = open('tcga_result_uuid.csv','a') 

for x,y,z in pool.imap(get_UUID, row_list):
	#print(x,y,z)
		ff.write(x)
		ff.write(',')
		ff.write(y)
		ff.write(',')
		ff.write(z)
		ff.write('\n')
		s += 1
		clock += 1
		if clock == 600:
			clock = 0
			print(s,'/',length)






