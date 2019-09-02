# -*- coding: utf-8 -*-
import pymysql as sql
import pandas as pd
import re
import pandas as pd
from pandas import Series,DataFrame

def conn_snp():

	db = sql.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="hgmd_pro")
	cursor=db.cursor()
	return db,cursor

'''
f = open('HGMD_mutation.tsv','a',encoding='utf-8')
db,cursor = conn_snp()
q = "SELECT * FROM hgmd_pro.mutation;"

cursor.execute(q)
snp = cursor.fetchall()
col = cursor.description

#print(list(snp[0]))

for i in col:
	t = list(i)
	f.write(t[0])
	f.write(',')
f.write('\n')

for line in snp:
	t = list(line)
	#print(t[0])
	for atom in t:
		f.write(str(atom))
		f.write('	')
	f.write('\n')

'''
def get_annotation():
	db,cursor = conn_snp()
	tar = "HGMD_mutation_utf_8.tsv"
	data = pd.read_csv(tar, sep='\t')
	data = DataFrame(data)
	print(data)
	result =pd.DataFrame(columns=('acc_num', 'chromosome', 'strand', 'coordSTART', 'coordEND', 'upstreamFLANK', 'downstreamFLANK'))	

	cursor = db.cursor(sql.cursors.DictCursor)
	acc_list = data['acc_num']
	key_list = ['acc_num', 'chromosome', 'strand', 'coordSTART', 'coordEND', 'upstreamFLANK', 'downstreamFLANK']
	for i in range(len(acc_list)):
		acc = acc_list[i]
		print(acc)
		q  = "SELECT * FROM hgmd_pro.hg19_coords where acc_num = '" + str(acc)+ "';"
		#print(q)
		cursor.execute(q)
		re = cursor.fetchall()
		try:	
			result = result.append(pd.DataFrame({'acc_num':[re[0]['acc_num']],'chromosome':[re[0]['chromosome']],'strand':[re[0]['strand']],'coordSTART':[re[0]['coordSTART']],'coordEND':[re[0]['coordEND']],'upstreamFLANK':[re[0]['upstreamFLANK']],'downstreamFLANK':[re[0]['downstreamFLANK']]}),ignore_index=True)
		except IndexError:
			result = result.append(pd.DataFrame({'acc_num':[acc],'chromosome':[''],'strand':[''],'coordSTART':[''],'coordEND':[''],'upstreamFLANK':[''],'downstreamFLANK':['']}),ignore_index=True)

		result.to_csv("mutation_hg19_coords_info.csv",index=0)
def get_annotation_hg38():
	db,cursor = conn_snp()
	tar = "HGMD_mutation_utf_8.tsv"
	data = pd.read_csv(tar, sep='\t')
	data = DataFrame(data)
	print(data)
	result =pd.DataFrame(columns=('acc_num_38', 'chromosome_38', 'strand_38', 'coordSTART_38', 'coordEND_38', 'upstreamFLANK_38', 'downstreamFLANK_38'))	

	cursor = db.cursor(sql.cursors.DictCursor)
	acc_list = data['acc_num']
	key_list = ['acc_num', 'chromosome', 'strand', 'coordSTART', 'coordEND', 'upstreamFLANK', 'downstreamFLANK']
	for i in range(len(acc_list)):
		acc = acc_list[i]
		print(acc)
		q  = "SELECT * FROM hgmd_pro.hg38_coords where acc_num = '" + str(acc)+ "';"
		#print(q)
		cursor.execute(q)
		re = cursor.fetchall()
		try:	
			result = result.append(pd.DataFrame({'acc_num_38':[re[0]['acc_num_38']],'chromosome_38':[re[0]['chromosome_38']],'strand_38':[re[0]['strand_38']],'coordSTART_38':[re[0]['coordSTART_38']],'coordEND_38':[re[0]['coordEND_38']],'upstreamFLANK_38':[re[0]['upstreamFLANK_38']],'downstreamFLANK_38':[re[0]['downstreamFLANK_38']],}),ignore_index=True)
		except IndexError:
			result = result.append(pd.DataFrame({'acc_num_38':[acc],'chromosome_38':[''],'strand_38':[''],'coordSTART_38':[''],'coordEND_38':[''],'upstreamFLANK_38':[''],'downstreamFLANK_38':[''],}),ignore_index=True)

		result.to_csv("mutation_hg38_coords_info.csv",index=0)

def get_annotation_mutnomen():
	db,cursor = conn_snp()
	tar = "HGMD_mutation_utf_8.tsv"
	data = pd.read_csv(tar, sep='\t')
	data = DataFrame(data)
	print(data)
	result =pd.DataFrame(columns=('acc_num', 'refCORE', 'refVER', 'cSTART', 'ivsSTART', 'cEND', 'ivsEND', 'wildBASE', 'mutBASE', 'protCORE', 'protVER', 'wildAMINO', 'mutAMINO', 'codon', 'hgvs', 'hgvsPROT', 'hgvsall'))	

	cursor = db.cursor(sql.cursors.DictCursor)
	acc_list = data['acc_num']
	key_list = ['acc_num', 'refCORE', 'refVER', 'cSTART', 'ivsSTART', 'cEND', 'ivsEND', 'wildBASE', 'mutBASE', 'protCORE', 'protVER', 'wildAMINO', 'mutAMINO', 'codon', 'hgvs', 'hgvsPROT', 'hgvsall']
	for i in range(len(acc_list)):
		acc = acc_list[i]
		print(acc)
		q  = "SELECT * FROM hgmd_pro.mutnomen where acc_num = '" + str(acc)+ "';"
		#print(q)
		cursor.execute(q)
		re = cursor.fetchall()
		try:	
			result = result.append(pd.DataFrame({'acc_num':[re[0]['acc_num']],'refCORE':[re[0]['refCORE']],'refVER':[re[0]['refVER']],'cSTART':[re[0]['cSTART']],'ivsSTART':[re[0]['ivsSTART']],'cEND':[re[0]['cEND']],'ivsEND':[re[0]['ivsEND']],'wildBASE':[re[0]['wildBASE']],'mutBASE':[re[0]['mutBASE']],'protCORE':[re[0]['protCORE']],'protVER':[re[0]['protVER']],'wildAMINO':[re[0]['wildAMINO']],'mutAMINO':[re[0]['mutAMINO']],'codon':[re[0]['codon']],'hgvs':[re[0]['hgvs']],'hgvsPROT':[re[0]['hgvsPROT']],'hgvsall':[re[0]['hgvsall']],}),ignore_index=True)
		except IndexError:
			result = result.append(pd.DataFrame({'acc_num':[acc],'refCORE':[''],'refVER':[''],'cSTART':[''],'ivsSTART':[''],'cEND':[''],'ivsEND':[''],'wildBASE':[''],'mutBASE':[''],'protCORE':[''],'protVER':[''],'wildAMINO':[''],'mutAMINO':[''],'codon':[''],'hgvs':[''],'hgvsPROT':[''],'hgvsall':[''],}),ignore_index=True)
		result.to_csv("mutation_mutnomen_info.csv",index=0)
def get_annotation_position():
	db,cursor = conn_snp()
	tar = "HGMD_mutation_utf_8.tsv"
	data = pd.read_csv(tar, sep='\t')
	data = DataFrame(data)
	print(data)
	result =pd.DataFrame(columns=('acc_num', 'position','descr'))
	cursor = db.cursor(sql.cursors.DictCursor)
	acc_list = data['acc_num']
	key_list = ['acc_num', 'position','descr']	
	total = len(acc_list)
	conut = 0
	s = 0
	for i in range(len(acc_list)):
		s = s + 1
		count = count + 1
		if conut == 500:
			print('#########  ',s,'/',total,'  ##########')
			count = 0
		acc = acc_list[i]
		#print(acc)
		q  = "SELECT acc_num,refseq,descr FROM hgmd_pro.allmut where acc_num = '" + str(acc)+ "';"
		#print(q)
		cursor.execute(q)
		re = cursor.fetchall()
		try:	
			result = result.append(pd.DataFrame({'acc_num':[re[0]['acc_num']],'position':[re[0]['position']],'descr':[re[0]['descr']],}),ignore_index=True)
		except IndexError:
			result = result.append(pd.DataFrame({'acc_num':[acc],'position':[''],'descr':[''],}),ignore_index=True)
		result.to_csv("mutation_position_info.csv",index=0)		

get_annotation_position()