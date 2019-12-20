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
	test_url = "https://dcc.icgc.org/api/v1/donors?filters={}&from=0&size=50"
	url_head = "ttps://dcc.icgc.org/api/v1/donors?filters={}&from="
	url_ass = "&size=50"
	for i in range(24289//50 +2):

		url = url_head + str(i) + url_ass
		r = requests.get(test_url)
		t = json.loads(r.text)
		for donor_info in t['hits']:
			f.write(str(donor_info) + '\n')
		if i % 20 == 0:
			print(i*50,' donor saved')

		





if __name__ == '__main__':
	main()