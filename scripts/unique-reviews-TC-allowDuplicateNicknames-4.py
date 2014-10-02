#!/usr/bin/env python

import time, sys, csv, xml, re, subprocess, random
import xml.etree.ElementTree as ET
from unidecode import unidecode

######################################
# Review Remover 
######################################

# file definitions
dymo_pr_file = 'review_data_complete.xml'
key_file = open('keys', 'w')
output_file = 'clean_pr_export_file.xml'
reviewers = {}
nicknames = set()

tree = ET.parse(dymo_pr_file)
root = tree.getroot()


for product in root.findall('product'):
	for review in product.find('reviews').findall('fullreview'):

		# get nickname, omitting spaces and converted to lowercase or set to Anonymous if nickname is missing				
		reviewer_id = review.find('merchantuserid').text 		
		location = review.find('location').text if not None else 'Anonymous'
		nick = review.find('nickname').text if not None else 'Anonymous'
		nick_decoded = unidecode(nick)
		revised_nick = re.sub("[^0-9a-zA-Z]", "", nick_decoded)
		if revised_nick == "":
			revised_nick = "Anonymous"
		if revised_nick != nick:
			print "Revising  nick from '" + nick.encode('utf-8') + "'' to '" + revised_nick + "'"
			review.find('nickname').text = revised_nick

		# set a random reviewer id if the existing id is either an email address or missing entirely
		# gkosan  TODO: what if we randomly assign the same ID to two different reviewers?  That might be bad...
		if reviewer_id is None or '@' in reviewer_id:
			reviewer_id = str(random.randint(1,9999999) * random.randint(1,9999999))	
			print "Changing missing reviewer_id to " + reviewer_id
			review.find('merchantuserid').text = reviewer_id

		else: # Unique nick, unique reviewer_key: Just file it
			nicknames.add(nick.lower())
			#reviewers[reviewer_key] = reviewer_id

	# END for review in product.find('reviews').findall('fullreview'):
# END for product in root.findall('product'):

tree.write(output_file, encoding="utf-8", xml_declaration=True, default_namespace='')				