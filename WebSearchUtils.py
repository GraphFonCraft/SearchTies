# coding=utf-8

from BeautifulSoup import BeautifulSoup
#from __future__ import print_function
from alchemyapi import AlchemyAPI

import urllib2
import random
import re
import json

def getTopDuck2GoUrls(queryString):
    queryTemplate = "http://duckduckgo.com/html/?q="
    queryUrl = queryTemplate + queryString
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

relatedUrls = getTopDuck2GoUrls("Печенька")
randomIndex = random.randint(0, len(relatedUrls) - 1)

print(getArticleText(relatedUrls[randomIndex]))