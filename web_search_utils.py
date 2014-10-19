# coding=utf-8

from BeautifulSoup import BeautifulSoup
#from __future__ import print_function
from alchemyapi import AlchemyAPI

import urllib2
import re
import json
import codecs
import os
import socket
import ssl

#from readability.readability import Document
#import urllib

def filterUrls(urls):
	urlReBlacklist = [
		"youtube.com",
		"vk.com",
		"mistudenti.ru",
		"2ch", 
		"dic.academic.ru"
	]

	badAssUrlIndex = []
	for i in range(len(urls)):
		for badAssUrl in urlReBlacklist:
			if (re.search(badAssUrl, urls[i])):
				badAssUrlIndex.append(i)

	for i in reversed(badAssUrlIndex):
		del urls[i]

	return urls

def getTopDuck2GoUrls(queryString):
	queryTemplate = "http://duckduckgo.com/html/?q="
	querryLocal = "&kl=ru-ru"
	queryUrl = queryTemplate + queryString + querryLocal
	site = urllib2.urlopen(urllib2.Request(queryUrl))
	
	try:
		htmlResponse = site.read()
	except socket.timeout, e:
		htmlResponse = ""
		pass
	except urllib2.URLError, e:
		htmlResponse = ""
		pass
	
	parsedResponse = BeautifulSoup(htmlResponse)
	links = []
	for i in parsedResponse.findAll('div', {'class': re.compile('links_main*')}):
		links.append( i.a['href'] )
	result = filterUrls(links)

	#print "Filtered stuff:"
	#for item in result:
	#	print item

	return result

def getSafeJustText(articleUrl):
	try:
		#print(articleUrl)
		text = urllib2.urlopen(articleUrl, timeout=1).read()
		charset = get_charset(text)
		#text = ""
		if not (charset is None):
			if re.match("^[\w\-]+$", charset):
				text = text.decode(charset)
			else:
				text = ""
		else:
			text = ""
		#	prog.match(string)
		
		#print(articleUrl)
	except socket.timeout, e:
		text = ""
		pass
	except urllib2.URLError, e:
		text = ""
		pass
	except ssl.SSLError, e:
		text = ""
		pass
	return text
	
def get_charset(header):
    match = re.search(r'charset=([^\s;]+)', header)
    if match:
        return match.group(1).strip('"\'').lower()
	
def printToFile(links):
	facts_urls = {}
	if len(links)>3:
		parse_pages_count = 3
	else:
		parse_pages_count = len(links)	

	if parse_pages_count > 0:
		for i in range(parse_pages_count): 
			a_text = getSafeJustText(links[i])
			#a_text = getFastText(links[i])
			text_patch = "/srv/http/app/texts/" + `i` 
			output_file = codecs.open(text_patch, 'w', "utf-8")
			output_file.write(a_text)
					
			facts_urls[i] = links[i]
			output_file.close()
			
	return facts_urls
			
#relatedUrls = getTopDuck2GoUrls("Печенька")
#randomIndex = random.randint(0, len(relatedUrls) - 1)
#print(getArticleText(relatedUrls[randomIndex]))
