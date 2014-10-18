# coding=utf-8

from BeautifulSoup import BeautifulSoup
import urllib2
import re

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

for link in  getTopDuck2GoUrls("Корова"):
    print link
