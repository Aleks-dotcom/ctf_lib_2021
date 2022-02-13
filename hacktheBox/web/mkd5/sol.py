import requests
import re
import hashlib
login_url = 'http://docker.hackthebox.eu:32601/'


conn = requests.Session()
login_page = conn.get(login_url)
string = login_page.text.splitlines()[5].split('>')[3].replace('</h3','')

md5 = hashlib.md5(string.encode('utf-8')).hexdigest()
data = {
	'hash':str(md5)
}
cookies = {
	'PHPSESSID':'doodf3akko2kbl929h6jm5oj70'
}

login_result = conn.post(login_url, data = data, cookies=cookies, allow_redirects = False)

print(login_result.text)
print(md5)

