from xml.dom.minidom import parse
from sets import Set

def parser(xmlfile):
	xmldoc = parse(xmlfile)
	itemlist1 = xmldoc.getElementsByTagName('Adj')
	itemlist2 = xmldoc.getElementsByTagName('Noun')
	
	list = Set()
	for i in range(len(itemlist1)):
		if i!= (len(itemlist1)-1):
			str = '"' + (itemlist1[i].attributes['val'].value).encode('utf-8') + " " + (itemlist2[i].attributes['val'].value).encode('utf-8') + '"'
			list.add(str)
	
	need_output = '{"id100" : {"source" : "http://" , "data" : [\n'
	i = 0
	for item in list:
		i+=1
		if i != len(list):
			need_output += item + ',\n '
		else:
			need_output += item 	

	need_output += '\n]}}'
	return need_output

#print(parser("/srv/http/app/facts/text"))