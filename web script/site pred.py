
'''
'mutation_cds', 'mutation_aa', 'fathmm_pred', 'sift_pred', 'provean_pred', 'polyphen2_hdiv_pred', 'polyphen2_hvar_pred', 'mutationtaster_pred', 'mutationassessor_pred', 'lrt_pred', 'metasvm_pred', \
'metalr_pred', 'm_cap_pred', 'fathmm_mkl_coding_pred', 'candra_category', 'condel_label', 'fathmm_cancer_pred', 'mutpred_label', 'genocanyon_label', 'cadd_label'


'''
import pymysql as sql
import pandas as pd
import re

def dictlist(tul,st1):
	tullist = list(tul)
	new_list = []
	for i in tullist:
		new_dict ={}
		j = 0
		temp = list(i)
		for k in st1:
			if j != 17:
				new_dict[k] = temp[j]
			else:
				new_dict[k] = temp[j][0:-1]
			j = j +1
		new_list.append(new_dict)
	return new_list
def judge(x,key):
	if not x:
		#print("null")
		return 0
	if (key == "polyphen2_hvar_pred" and (x == "P" or x == "D")):
		return 1
	elif (key == "polyphen2_hdiv_pred" and (x == "P" or x == "D")):
		return 1
	elif (key == "mutationassessor_pred" and (x == "H" or x == "M" or x == "L")):
		return 1
	elif (key == "mutationtaster_pred" and (x == "A" or x == "D")):
		return 1
	elif (x == "Driver" or x == "D"):
		return 1
	else:
		return -1

	
	

def GetAndSave(dictlist,tab,l,predictMethods,st1):
	predtxtname = "D:/site/pred/" + l + "_pred" + tab[14:] + ".txt"
	#print(predtxtname)
	pred_d =[]
	pred_n = []
	for i in range(len(st1)):
		pred_d.append(0)
		pred_n.append(0)

	
	for i in dictlist:
		k = 0
		#print(i)
		for j in st1:

			pred = i[j]
			pred_result = judge(pred,j)
			if pred_result == 1:
				pred_d[k] = pred_d[k] + 1
			elif pred_result == -1:
				pred_n[k] = pred_n[k] + 1
			k = k + 1

	ff = open(predtxtname, 'w')
	for i in pred_d:
		ff.write(str(i))
		ff.write(",")
	ff.write("\n")
	for i in pred_n:
		ff.write(str(i))
		ff.write(",")
	ff.write("\n")
	for i in predictMethods:
		ff.write(i)
		ff.write(",")
	ff.close()
	print(predtxtname,"-----done")













db = sql.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB_new")
cursor=db.cursor()

q ="select FATHMM_pred,SIFT_pred,PROVEAN_pred,Polyphen2_HDIV_pred,Polyphen2_HVAR_pred,MutationTaster_pred,MutationAssessor_pred,LRT_pred,MetaSVM_pred,MetaLR_pred,`M-CAP_pred`,`fathmm-MKL_coding_pred`,CanDrA_Category,CONDEL_LABEL,FATHMM_Cancer_pred,MutPred_LABEL,GenoCanyon_LABEL,CADD_LABEL from all_info_order_by_site_"



st ="'fathmm_pred', 'sift_pred', 'provean_pred', 'polyphen2_hdiv_pred', 'polyphen2_hvar_pred', 'mutationtaster_pred', 'mutationassessor_pred', 'lrt_pred', 'metasvm_pred', \
'metalr_pred', 'm_cap_pred', 'fathmm_mkl_coding_pred', 'candra_category', 'condel_label', 'fathmm_cancer_pred', 'mutpred_label', 'genocanyon_label', 'cadd_label'" #18
w = " where `Primary site` = '"

st1 = st.split(",")
for i in range(len(st1)):
	if i != 0:
		st1[i] = st1[i][2:-1]

st1[0] = st1[0][1:-1]
predictMethods = []
for x in st1:
	predictMethods.append(str(x.replace('_pred','')))

#st1 is the key
tablist = ["m","s","u"]
for j in tablist:
	f = open('D:/sitename.txt', 'r')
	tab = "all_info_order_by_site_" + j
	l = f.readline()  #l =site
	while l:
		l = l[0:-1]
		#print(l+tab)



		
		tosql = q + j + w + l + "'"
		cursor.execute(tosql)
		pred = cursor.fetchall()
		#print(tosql)
		#print(pred)
		pred_dict_list = dictlist(pred,st1)
		#print(pred_dict_list)
		GetAndSave(pred_dict_list,tab,l,predictMethods,st1)
		




		l = f.readline() 




#cursor.execute(q+w)
#pred = cursor.fetchall()


#print(st1,len(st1))