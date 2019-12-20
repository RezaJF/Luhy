import requests
import json
def test():
	total_doner = 24289
	test_url = "https://dcc.icgc.org/api/v1/donors?filters={}&from=0&size=50"
	r = requests.get(test_url)
	t = json.loads(r.text)
	for donor_info in t['hits']:
		print(donor_info)


def main():
	f = open('donorInfo.txt','w')
	total_doner = 24289
	#test_url = "https://dcc.icgc.org/api/v1/donors?filters={}&from=0&size=50"
	url_head = "https://dcc.icgc.org/api/v1/donors?filters={}&from="
	url_ass = "&size=50"
	for i in range(total_doner//50 +1):

		url = url_head + str(i*50) + url_ass
		r = requests.get(url)
		t = json.loads(r.text)
		for donor_info in t['hits']:
			f.write(str(donor_info) + '\n')
		if i % 20 == 0:
			print(i*50,' donor saved')
	print(url)
if __name__ == '__main__':
	main()