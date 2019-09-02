import os 
import pandas as pd
def dataFrameClean():
	d2 = pd.read_table('unip_info/unip_pdb_site.txt',sep='\t',dtype='str',error_bad_lines=False )
	#f = open("unip_pdb_site.txt","r")
	list1= []
	for index, row in d2.iterrows():
		if len(row['UniProt']) > 20: 
			d2.drop(index,axis=0,inplace=True)
	d2.to_csv('unip_pdb_site_clean.csv',index=0)
	#d2.close()







def mergeall():
	d2 = pd.read_table('unip_pdb_site_clean.csv',sep=',',dtype='str',error_bad_lines=False)
	d1 = pd.read_table('unip_info/resultsFromSIFTS_6_mo_2.csv',sep=',',dtype='str',error_bad_lines=False)

	result = pd.merge(d1, d2, how='inner', on=['pdb', 'chain_id','UniProt'])

	result.to_csv('merge.csv',index=0)
	#print(d1.keys())
	#print(d2)
	#for index, row in d1.iterrows():
def Bin(base,real):
	b_start = base[0]
	b_end = base[-1]
	binlist=""
	for i in range(b_start,b_end+1):
		temp = str(i)
		if temp not in real:
			binlist += "0"
		else:
			binlist += "-"
	return binlist

def jiaoji(list1,list2):
	jj = []
	for i in list1:
		if i in list2 and i not in jj:
			jj.append(i)
	return jj


def nor():

	d1 = pd.read_table('merge.csv',sep=',',dtype='str',error_bad_lines=False)
	list1= []
	d1["len_diff"] = None
	
	d1["u_len"] = None
	d1["u_r_len"] = None
	
	d1["large_loss"] = None
	d1["class"] = None
	d1["bin"] = None
	for index, row in d1.iterrows():
		us = int(row["unp_start"])
		ud = int(row["unp_end"])
		ur = row["unip_site"]
		u_list = []
		for i in range(us,ud+1):
			u_list.append(i)
		
		u_r_list = ur.split(",")
		#print(len(u_list)-len(u_r_list))
		row["len_diff"] = len(u_list)-len(u_r_list)
		row["u_len"] = len(u_list)
		row["u_r_len"] = len(u_r_list)
		if (abs(row["len_diff"] / len(u_list)) > 0.8 or abs(row["len_diff"] / len(u_r_list))> 0.8) and (len(u_list)< 50 or len(u_r_list)<50):
			row["class"] = "length not match"
		#print(type(u_list[0]),type(u_r_list[0]))
		row["bin"] = Bin(u_list,u_r_list)



	d1.to_csv('merge_1.csv',index=0)
	
	#print(d1)

#dataFrameClean()
#mergeall()

#nor()
list1 = ["a","b","c"]
list2 =["b","c","d"]
neel =jiaoji(list1,list2)
print(neel)
