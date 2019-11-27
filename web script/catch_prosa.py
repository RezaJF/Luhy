import requests
import json

url = 'https://prosa.services.came.sbg.ac.at/prosa.php'

data = {"pdbCode":'3WSQ',"chainID":'A'}
header = {'Referer':'https://prosa.services.came.sbg.ac.at/prosa.php','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
req = requests.post(url,data)
#req = requests.get(url)
print(req.text)