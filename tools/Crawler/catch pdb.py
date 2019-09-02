import requests
import time
import re
import paramiko
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

def work(pdb):
	url = "http://servicesn.mbi.ucla.edu/SAVES/"
	file ={'pdbfile':'pdb/SMR_A0PJY2-2_4.pdb'} 
	r = requests.post(url,files = file)
	print(r.text)

#work(1)
def seleWork(pdbpath):
	keyword ="http://servicesn.mbi.ucla.edu/Verify3D/downloaddata?job="
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
	#driver.set_window_size(800, 600)
	driver.get("http://servicesn.mbi.ucla.edu/SAVES")
	#
	#print(driver.title)
	upload = driver.find_element_by_id('pdbfile')
	#print(upload)
	upload.send_keys(pdbpath)
	#print(upload.get_attribute('value'))
	driver.find_element_by_id("dojob").send_keys(Keys.ENTER)
	time.sleep(30)
	pageSource = driver.page_source
	pageSource=str(pageSource.encode("GBK", 'ignore'))
	#print(pageSource)
	index = pageSource.find(keyword)
	if index != -1:

		jobid = re.sub("\D", "", pageSource[index+len(keyword):index+len(keyword)+8])
		#print(jobid)
	else:
		jobid = 0

	driver.close()
	print(pdbpath,' : ',jobid)
	return jobid
def copypdb(pdblist):
	host_name = '10.20.213.14'
	user_name = 'wangs'
	password = '123456'
	remote_dir2 = '/home/zzf/Work/Filter_GetMaterials_0327/ModBase_modelSet_r/'
	remote_dir1 = '/home/zzf/Work/Filter_GetMaterials_0327/SMR_modelSet_r/'
	local_dir1 = 'pdb/SMR'
	local_dir2 = 'pdb/ModBase'
	port =22
	t=paramiko.Transport((host_name,port))
	t.connect(username=user_name,password=password)
	sftp=paramiko.SFTPClient.from_transport(t)
	for i in pdblist:
		print(i,",done")
		#if i[0] == "S":
			#sftp.get(os.path.join(remote_dir1,i),os.path.join(local_dir1,i))
		if i[0] == "m":
			temp = i[:-1]
			sftp.get(os.path.join(remote_dir2,temp),os.path.join(local_dir2,temp))
		
	t.close()


def getlist(f):
	f1 = open(f,"r")
	l = f1.readline()
	l = f1.readline()
	pdblist = []
	while l:
		temp = l.split(" ")
		#print(temp[0],temp[1])
		pdblist.append(temp[0])
		pdblist.append(temp[1])
		l = f1.readline()
	print(pdblist)
	return(pdblist)


def getmisslist(f):
	f1 = open(f,"r")
	l = f1.readline()
	pdblist = []
	while l:
		pdblist.append(l[:-1])
		l = f1.readline()
	print(pdblist)
	return pdblist


		



#seleWork()
#path =pdb/SMR_A0PJY2-2_4.pdb
f = "result_miss_pdbmod.txt"
#pdblist = getlist(f)
#copypdb(pdblist)
pdblist = getmisslist(f)
t = 1
result = []
for i in pdblist:
	if i[0] == "S":
		pdbpath = "pdb/SMR/" + i
	if i[0] == "m":
		pdbpath = "pdb/ModBase/" + i[:-1]
	jobid = seleWork(pdbpath)
	result.append(i)
	result.append(str(jobid))
	print("***************",t,"/",len(pdblist),"***************")
	t+=1
'''
f2 = open('jobid.txt','w')
s =1
for i in result:
	f2.write(i)
	f2.write(',')
	if s == 4:
		f2.write("\n")
		s = 1
	s += 1

'''










