import requests
from bs4 import BeautifulSoup
import json


def get(url):
	r = requests.get(url)
	print(len(r.text))
	a =r.text
	f= open("1.html","w")
	f.write(a)



url ="http://mdl.shsmu.edu.cn/asbench/module/complex/complex.jsp?record_id=AS001000501_3UO9"
get(url)