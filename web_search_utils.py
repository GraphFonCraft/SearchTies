# coding=utf-8

from BeautifulSoup import BeautifulSoup
#from __future__ import print_function
from alchemyapi import AlchemyAPI

import urllib2
import random
import re
import json
import codecs
import os
import socket

from readability.readability import Document
#import urllib

def getTopDuck2GoUrls(queryString):
	queryTemplate = "http://duckduckgo.com/html/?q="
	querryLocal = "&kl=ru-ru"
	queryUrl = queryTemplate + queryString + querryLocal
	site = urllib2.urlopen(urllib2.Request(queryUrl))
	htmlResponse = site.read()
	
	parsedResponse = BeautifulSoup(htmlResponse)
	links = []
	for i in parsedResponse.findAll('div', {'class': re.compile('links_main*')}):
		links.append( i.a['href'] )
	return links

def old_getArticleText(articleUrl):
    alchemyapi = AlchemyAPI()
    response = alchemyapi.text('url', articleUrl)

    return response['text'].encode('utf-8')

def getSafeJustText(articleUrl):
	try:
		text = (urllib2.urlopen(articleUrl, timeout=1).read()).encode('utf-8')
	except socket.timeout, e:
		text = ""
		pass
	except urllib2.URLError, e:
		text = ""
		pass
	return text

def old_getFastText(articleUrl):
	print("start" + articleUrl)
	html = urllib2.urlopen(articleUrl, timeout=1).read()
	readable_article = Document(html).summary()
	return readable_article.encode('utf-8')
	
def printToFile(links):
	facts_urls = {}
	if len(links)>3:
		parse_pages_count = 3
	else:
		parse_pages_count = len(links)	

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