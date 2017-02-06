import requests
import sys
import urllib2
import contextlib
import json
import os

from secrets import secret, uid

class Student:
	def __init__(self, name, uid, level):
		self.name = name
		self.uid = uid
		self.level = level

r = requests.post("https://api.intra.42.fr/oauth/token", data={'grant_type': 'client_credentials', 'client_id': uid, 'client_secret': secret})
r.raise_for_status()
access_token = r.text[17:81]
print access_token

# piscine = "Exams"
# year = "2016"

# url = 'https://api.intra.42.fr/v2/cursus/1/exams?access_token=' + access_token
# events = []

# t = 1
# page = 1
# while t:
# 	with contextlib.closing(urllib2.urlopen(url + "&page=" + str(page))) as x:
# 		result = json.load(x)
# 	if result:
# 		events += result
# 	else:
# 		t = 0
# 	print "Parsed page", page
# 	page += 1

# ordered = []
# if not os.path.exists(piscine + "/"):
#     os.makedirs(piscine + "/")
# for event in events:
# 	if not os.path.exists(piscine + "/" + str(event['id'])):
# 		with open(piscine + "/" + str(event['id']), 'w') as f:
# 			json.dump(event, f)
# 			print "Added", str(event['id'])