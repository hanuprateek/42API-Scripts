import requests
import sys
import urllib2
import contextlib
import json
import os
from collections import Counter
from tabulate import tabulate

piscine = "/July/"
print "\n\n--------------July--------------"
for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for project in user['projects_users']:
				if project['project']['id'] == 26:
					print user['login'] + "  -  " + project['status']
		except:
			print filename + "------------------------ fail -------------------------"

piscine = "/August/"
print "--------------August--------------"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for project in user['projects_users']:
				if project['project']['id'] == 26:
					print user['login'] + "  -  " + project['status']
		except:
			print filename + "------------------------ fail -------------------------"

piscine = "/October/"
print "\n\n--------------October--------------"
for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for project in user['projects_users']:
				if project['project']['id'] == 26:
					print user['login'] + "  -  " + project['status']
		except:
			print filename + "------------------------ fail -------------------------"

piscine = "/January/"
print "\n\n--------------January--------------"
for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for project in user['projects_users']:
				if project['project']['id'] == 26:
					print user['login'] + "  -  " + project['status']
		except:
			print filename + "------------------------ fail -------------------------"
