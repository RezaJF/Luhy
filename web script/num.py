


def num(string):

	num_list =string.split(",")
	n_list = []
	for i in num_list:
		if i.find("-") != -1:
			#print(i)
			temp = i.split("-")
			a1 = int(temp[0])
			a2 = int(temp[1])
			for j in range(a1,a2+1,1):
				n_list.append(j)
				#print(j)
		else:
			a3 = int(i)
			n_list.append(a3)

	return n_list














#####################main############################ 
old_list = "19,21-23,91,93-98,101-104,114-123,130-131,136-140,150,152-153,164-171,174,177-178,180-181,186-187,191,198-201,208-209,212,219,221-228,231,233,239,241,243-244,247-248,250,259-261,263-264,273,276-277,280,283-291,305-306,321,323-335,337-351,382-384"
n = 999
l = num(old_list)
print(l)
if n in l:
	print("yes")
else:
	print("no")
