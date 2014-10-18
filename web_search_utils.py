# coding=utf-8

from BeautifulSoup import BeautifulSoup
#from __future__ import print_function
from alchemyapi import AlchemyAPI

import urllib2
import random
import re
import json
import codecs

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

def getArticleText(articleUrl):
    alchemyapi = AlchemyAPI()
    response = alchemyapi.text('url', articleUrl)

    return response['text'].encode('utf-8')

def getSoupArticleText(articleUrl):
    return "AlternativeFastFunc"
	
def printToFile(links):
	output_file = codecs.open("/srv/http/app/texts/text",'w', "utf-8")
	for i in range(3): #3 for debug
		a_text = getArticleText(links[i])
		output_file.write(a_text)
	
	output_file.close()
			
#relatedUrls = getTopDuck2GoUrls("Печенька")
#randomIndex = random.randint(0, len(relatedUrls) - 1)
#print(getArticleText(relatedUrls[randomIndex]))