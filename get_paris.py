from threading import Thread, enumerate
import requests
import sys
import urllib2
import contextlib
import json
import os
import datetime
from threading import Thread

from secrets import secret, uid

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
count = 0

api_url = "https://api.intra.42.fr/oauth/token"
creds_obj = {'grant_type': 'client_credentials', 'client_id': uid, 'client_secret': secret}
r = requests.post(api_url, data=creds_obj)
r.raise_for_status()
access_token = r.text[17:81]
url = "https://api.intra.42.fr/v2/cursus/1/users?access_token=" + access_token + "&page="
profiles = []

page = 1
print access_token
while True:
	response = urllib2.urlopen(url + str(page))
	data = json.loads(response.read())
	if data:
		profiles += data
	else:
		break
	print "Fetched data from page", page
	page += 1

if not os.path.exists("Paris/"):
	os.makedirs("Paris/")

def create_file(user, count, total):
	if os.path.exists("Paris/" + user["login"]):
		st = os.stat("Paris/" + user["login"])
		mtime = datetime.datetime.fromtimestamp(st.st_mtime)
	else:
		mtime = yesterday
	if mtime <= yesterday:
		response = urllib2.urlopen(user["url"] + "?access_token=" + access_token)
		data = json.loads(response.read())
		with open("Paris/" + data["login"], 'w') as f:
			json.dump(data, f)
		print "Added Profile", count, "of", total, user["login"]

threads = []
for user in profiles:
	count += 1
	process = Thread(target=create_file, args=[user, count, len(profiles)])
	process.start()
	threads.append(process)

for process in threads:
    process.join()
