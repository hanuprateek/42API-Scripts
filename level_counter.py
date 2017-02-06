import requests
import sys
import urllib2
import contextlib
import json
import os
from collections import Counter
from tabulate import tabulate

piscine = "/August/"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		# try:
			user = json.load(data)
			for data in user['cursus_users']:
				if data['level'] >= 7.0 and data['cursus_id'] == 1:
					print data['user']['login'] + " - level : " + str(data['level'])

piscine = "/July/"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for data in user['cursus_users']:
				if data['level'] >= 7.0 and data['cursus_id'] == 1:
					print data['user']['login'] + " - level : " + str(data['level'])
		except:
			print filename + "------------------------ fail -------------------------"

piscine = "/October/"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for data in user['cursus_users']:
				if data['level'] >= 7.0 and data['cursus_id'] == 1:
					print data['user']['login'] + " - level : " + str(data['level'])
		except:
			print filename + "------------------------ fail -------------------------"

piscine = "/January/"

for filename in os.listdir(os.getcwd() + piscine):
	with open(os.getcwd() + piscine + filename) as data:
		try:
			user = json.load(data)
			for data in user['cursus_users']:
				if data['level'] >= 7.0 and data['cursus_id'] == 1:
					print data['user']['login'] + " - level : " + str(data['level'])
		except:
			print filename + "------------------------ fail -------------------------"
