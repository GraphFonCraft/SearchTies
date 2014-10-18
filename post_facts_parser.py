from xml.dom.minidom import parse
from sets import Set

def parser(xmlfile, query):
	xmldoc = parse(xmlfile)
	itemlist1 = xmldoc.getElementsByTagName('Adj')
	itemlist2 = xmldoc.getElementsByTagName('Noun')
	
	list = Set()
	for i in range(len(itemlist1)):
		if i!= (len(itemlist1)-1):
			str = (itemlist1[i].attributes['val'].value).encode('utf-8') + " " + (itemlist2[i].attributes['val'].value).encode('utf-8')
			list.add(str)
	
	need_output = '{"query" : "'+ query +'", "data" : ['
	i = 0
	source = "http://wqrqwfasf.asfasf/asfas"
	weight = 5
	for item in list:
		i+=1
		need_output += '{ "title" : "'+item+'", "source" : "'+ source +'", "weight" : "'+ `weight` +'" }'
		if i != len(list):
			need_output += ', '	

	need_output += ']}'
	return need_output

#print(parser("/srv/http/app/facts/text"))