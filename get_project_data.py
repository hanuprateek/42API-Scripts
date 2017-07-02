import requests
import sys
import urllib2
import contextlib
import json
import os
from collections import Counter
from tabulate import tabulate

piscine = "/Paris/"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for project in user['projects_users']:
				if project['project']['id'] == 58 and project['final_mark'] >= 90:
					print user['login'] + "  -  " + str(project['final_mark']) + "  -  " + str(project['id'])
		except:
			print filename + "------------------------ fail -------------------------"
