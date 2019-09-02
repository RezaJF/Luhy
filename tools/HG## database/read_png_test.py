import pytesseract
from PIL import Image
import os 
import paramiko
import shutil
#image = Image.open("87608_M2.png")

#image.show()
#text = pytesseract.image_to_string(image,lang='eng')
#print(text)
def save():
	file_dir = r"D:\database\img_to_text"

	for root, dirs, files in os.walk(file_dir):
		print(files)

	f = open("png_to_text_result.txt","w")
	for png in files:
		#print(png[-3:])
		if png[-3:] == 'png':
			image = Image.open(png)
			text = pytesseract.image_to_string(image,lang='eng')
			print(png,text)
			f.write(png)
			f.write(",")
			f.write(text)
			f.write('\n')

def serverConnect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    ssh.connect(hostname='10.20.212.153', port=22, username='Luhy', password='lhy123')
    return ssh
ssh = serverConnect()

def copy():

	host_name = '10.20.212.153'
	user_name = 'Luhy'
	password = 'lhy123'

	remote_dir1 = '/data/wangs/MutaAnalysis/three.data0223/output/compare_data_with_hgmd/imgs/'
	local_dir1 = 'D:/database/img_to_text'
	port =22
	t=paramiko.Transport((host_name,port))
	t.connect(username=user_name,password=password)
	sftp=paramiko.SFTPClient.from_transport(t)

	file_dir = r"D:\database\img_to_text"

	for root, dirs, files in os.walk(file_dir):
		f_list = files
	ssh = serverConnect()
	stdin, stdout, stderr = ssh.exec_command('ls /data/wangs/MutaAnalysis/three.data0223/output/compare_data_with_hgmd/imgs/')
	res_list = stdout.readlines()
	print(res_list[0])

	print(f_list[0])
	for png_153 in res_list:
		temp = png_153[0:-1]
		#print(temp)
		if temp not in f_list:
			
			sftp.get(os.path.join(remote_dir1,temp),os.path.join(local_dir1,temp))
			print(temp)

def fix():
	lib2=["Gly","Ala","Val","Leu","Ile","Pro","Phe","Tyr","Trp","Ser","Thr","Cys","Met","Asn","Gln","Asp","Glu","Lys","Arg","His"]
	error_list = []
	error_ex = []
	empty_list = []
	f = open("png_to_text_result.txt","r") 
	list1 = f.readlines()
	#print(list1)
	for i in list1:
		temp = i.split(',')
		name =  temp[0]
		text = temp[1][:-1]
		#print(name)
		#print(text)
		if name[-5] == '2':
			try:
				aa = text.split('-')
				if aa[0] not in lib2:
					if aa[0] not in error_list:
						error_list.append(aa[0])
						error_ex.append(name)
				if aa[1] not in lib2:
					if aa[1] not in error_list:
						error_list.append(aa[1])
						error_ex.append(name)
			except IndexError:

				empty_list.append(name)




	print(error_list)
	#print(empty_list)
	print(error_ex)

def fixAA():
	cannot_read_list = []
	error_list =['val', 'ala', 'Tern', 'Aarg', '', 'Thr=', 'Het', 'fsn', 'arg', 'Thr=Lys', 'vVal', 'Tle']
	fix_list = ['Val','Ala','Term','Arg','error','Thr','Met','Asn','Arg','Thr-Lys','Val','Ile']

	lib2=["Gly","Ala","Val","Leu","Ile","Pro","Phe","Tyr","Trp","Ser","Thr","Cys","Met","Asn","Gln","Asp","Glu","Lys","Arg","His"]

	f = open("png_to_text_result.txt","r") 
	ff = open("fix_AA_error_text.txt","w")
	
	list1 = f.readlines()
	for i in list1:
		temp = i.split(',')
		name =  temp[0]
		text = temp[1][:-1]
		fix_text = text
		if name[-5] == '2':
			aa = text.split('-')
			if len(aa) == 2:
				if aa[0] not in lib2:
					for j in range(len(error_list)):
						if error_list[j] == aa[0]:
							aa[0] = fix_list[j]
				if aa[1] not in lib2:
					for j in range(len(error_list)):
						if error_list[j] == aa[1]:
							aa[1] = fix_list[j]
				fix_text = aa[0] + "-" + aa[1]
			else:
				if text == "":
					fix_text = "cannot_read"
					cannot_read_list.append(name)
				if text == "Thr=Lys":
					fix_text = "Thr-Lys"

			ff.write(name)
			ff.write(",")
			ff.write(fix_text)
			ff.write("\n")

	print("empty:")
	print(cannot_read_list)









'''
def move(list1):
	for i in list1:
		i_c = "D:/database/img_to_text" + '/' + i
		i_d = "D:/database/img_to_text/ex" + '/' + i
		print(i_d)
		shutil.copy(i_c,i_d)　
	return 0
'''

#copy()
#save()
#fix()

error_list =['val', 'ala', 'Tern', 'Aarg', '', 'Thr=', 'Het', 'fsn', 'arg', 'Thr=Lys', 'vVal', 'Tle']
fix_list = ['Val','Ala','Term','Arg','error','Thr','Met','Asn','Arg','Thr-Lys','Val','Ile']
error_ex = ['104597_M2.png', '104597_M2.png', '104607_M2.png', '104615_M2.png', '107725_M2.png', '107726_M2.png', '107729_M2.png', '112209_M2.png', '112246_M2.png', '112600_M2.png', '114472_M2.png', '17961_M2.png']
#a = move(error_ex)

fixAA()


