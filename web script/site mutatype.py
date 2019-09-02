import pymysql as sql
import pandas as pd
import re


def getsite():
	q ="SELECT DISTINCT `Primary site` from all_info_order_by_site_m;"
	cursor.execute(q)
	site = cursor.fetchall()
	f2=open('D:/sitename.txt', 'w')
	site =list(site)
	print(len(site))
	for i in site:
		temp = str(i)
		temp = temp[2:-1]
		temp = temp[0:-2]
		print(temp)

		f2.write(temp)
		f2.write("\n")

def t2d(cds):
	cds = list(cds)
	n_list = []
	for i in cds:
		temp = str(i)
		temp = temp[-6:-3]
		n_list.append(temp)
	varientTypes = set(n_list)
	varientStat = {}
	for x in varientTypes:
		varientStat[x] = n_list.count(x)


	return list(varientTypes), varientStat

def savedata(varientTypes,varientStat,l,tab):
	typetxtname = "D:/site/" + l + "_variant_type" + tab[14:] + ".txt"
	stattxtname = "D:/site/" + l + "_variant_stat" + tab[14:] + ".txt"
	ff1 = open(typetxtname, 'w')
	ff2 = open(stattxtname, 'w')
	for i in varientTypes:
		ff1.write(i)
		ff1.write(",")
	ff1.close()
	ff2.write(str(varientStat))
	ff2.close()
	print(typetxtname,"-----done")

	
db = sql.connect(host="10.20.212.172",user="varientdb",passwd="varient2017",db="varientDB_new")
cursor=db.cursor()
#getsite()


tablist = ["m","s","u"]
for j in tablist:
	f = open('D:/sitename.txt', 'r')
	tab = "all_info_order_by_site_" + j
	l = f.readline()        #l =site

	while l:
		l = l[0:-1] 
		
		s1 = "SELECT `Mutation CDS` from " + tab + " where `Primary site` = "

		s = s1 + "'" + l + "'"
		#print(s)

		f3 = open('D:/sitemutaCDs.txt', 'w')
		cursor.execute(s)
		cds = cursor.fetchall()
		#print(cds)
		varientTypes,varientStat = t2d(cds)
		#print(n_list)
		#print(varientTypes)
		#print(varientStat)
		savedata(varientTypes,varientStat,l,tab)
		l = f.readline()
	f.close()





