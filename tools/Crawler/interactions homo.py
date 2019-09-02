
'''
f = open("interactions.dat","r")
l = f.readline()
l = f.readline()
temp = l.split("	")

print(temp[0],temp[])

'''

f=open("UniprotID_list.txt","r")
l = f.readline()
unilist = []
while l:
	if "-" in l:

		temp = l.split("-")[0]
	else:
		temp = l[:-1]
	if temp not in unilist:
		unilist.append(temp)
	l = f.readline()
#print(unilist)
f.close()
ff = open("interactions.dat","r")
fff = open("interactions_uniprot.txt","w")
cl = open("clean_uni_list.txt","w")
for i in unilist:
	cl.write(i)
	cl.write("\n")
cl.close()
l = ff.readline()
l = ff.readline()

while l:
	temp = l.split("	")
	if temp[0] != temp[1]:
		if (temp[0] in unilist):
			fff.write(l)
		elif (temp[2] in unilist):
			fff.write(l)

		#fff.write("\n")



	l = ff.readline()
