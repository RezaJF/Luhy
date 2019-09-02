import requests
from bs4 import BeautifulSoup
import json


def get(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	new_list = []
	for link in soup.find_all('font'):
		temp_dict = {}

		#sty = link.get('style')
		#col = link.get('color')
		#if sty == "cursor:pointer;cursor:hand"
		try:
			a =link.string
			sty = link.get('style')
			col = link.get('color')
			if sty == 'cursor:pointer;cursor:hand':
				if col == 'red':
					tempcol = "red"
					tempchar = a

					temp_dict ={tempchar:tempcol}
				else:
					tempcol = "black"
					tempchar = a

					temp_dict ={tempchar:tempcol}
			if temp_dict != {}:	
				new_list.append(temp_dict)			

			#print(a)
		except(UnicodeEncodeError):
			print("!!!")
	return new_list










url ="http://denglab.org/cgi-bin/PrabHot/results.cgi?jobid=RH0710027"

list1 = get(url)
print(list1)



