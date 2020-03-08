# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os
import re
import requests

def getGitusers(mail):
	global usename
	print (mail)
	os.system("echo "+mail+" > 1.txt")
	os.system("git add 1.txt")
	os.system("git config user.email {mail}".format(mail=mail))
	res = os.popen("git commit -m '"+mail+"'" ).read()
	gitCommit = res[8:15]
	os.popen("git push")
	try:
		html = requests.get("https://github.com/Rainism/test/commits",verify=False).content
		username = re.findall(r'/Dawson0x00/test/commits\?author=(.*?)\"',html)
		print (usename)
	except Exception as e:
		print(e)
		pass
	return username


if __name__ == '__main__':
	global usename
	with open('email.txt') as f:
		for email in f.readlines():
			email = email.strip()
			usename = getGitusers(email)
			print(email+': '+str(usename))