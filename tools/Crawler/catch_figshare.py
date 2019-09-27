import json
import requests
import pandas as pd
from pandas import Series,DataFrame

url_list = ["https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3Afalse%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783192",\
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A2480%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783193",\
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A2381%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783194",
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A1741%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783195",
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A932%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783196",
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A765%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783197",
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A552%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783198",
"https://hgv.figshare.com/api/genes/public_listing?params_json=%7B%22last_id%22%3A13%2C%22batch_size%22%3Afalse%2C%22sort_by%22%3A%7B%22by%22%3Afalse%2C%22type%22%3A%22asc%22%7D%2C%22filters%22%3A%7B%22region_id%22%3Afalse%2C%22mutation_type_id%22%3A%2221%22%2C%22zygosity_id%22%3Afalse%7D%2C%22search_term%22%3Afalse%2C%22advanced_search%22%3A%5B%5D%7D&_=1568856783199"]
result =pd.DataFrame(columns=('note', 'doi', 'zygosity', 'name', 'reference', 'region', 'codon', 'disease', 'author_name', 'mutation_type', 'genome_position', 'omim', 'omim2', 'ethnicity', 'gene_bank_number', 'protein', 'de_novo', 'id', 'chromosome', 'mutation'))
col_list = ['note', 'doi', 'zygosity', 'name', 'reference', 'region', 'codon', 'disease', 'author_name', 'mutation_type', 'genome_position', 'omim', 'omim2', 'ethnicity', 'gene_bank_number', 'protein', 'de_novo', 'id', 'chromosome', 'mutation']

for url in url_list:
	
	r = requests.get(url)
	t = json.loads(r.text)
	print(t['items'][0].keys())

	for var in t['items']:
		result = result.append(pd.DataFrame({'note':[var['note']],'doi':[var['doi']],'zygosity':[var['zygosity']],'name':[var['name']],'reference':[var['reference']],'region':[var['region']],'codon':[var['codon']],'disease':[var['disease']],'author_name':[var['author_name']],'mutation_type':[var['mutation_type']],'genome_position':[var['genome_position']],'omim':[var['omim']],'omim2':[var['omim2']],'ethnicity':[var['ethnicity']],'gene_bank_number':[var['gene_bank_number']],'protein':[var['protein']],'de_novo':[var['de_novo']],'id':[var['id']],'chromosome':[var['chromosome']],'mutation':[var['mutation']],}),ignore_index=True)


result.to_csv("figshare.csv",index=0)
