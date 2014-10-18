from xml.dom.minidom import parse
#from sets import Set

def parser(xml_file_dir, query, facts_urls):
	#read facts
	list = {}
	for file_index in facts_urls:
		xmldoc = parse(xml_file_dir+`file_index`)
		itemlist1 = xmldoc.getElementsByTagName('Adj')
		itemlist2 = xmldoc.getElementsByTagName('Noun')
			
		for i in range(len(itemlist1)):
			str = (itemlist1[i].attributes['val'].value).encode('utf-8') + " " + (itemlist2[i].attributes['val'].value).encode('utf-8')
			list[str] = file_index
	
	#weight mod by domain
	weight = {}
	for file_index in facts_urls:
		weight[file_index] = 5
		if (facts_urls[file_index]).find("ru.wikipedia.org") != -1:
			weight[file_index] = 7
		if (facts_urls[file_index]).find("lurkmore.to")!= -1:
			weight[file_index] = 3
		if (facts_urls[file_index]).find("absurdopedia.net")!= -1:
			weight[file_index] = 3
			
	#json output
	need_output = '{"query" : "'+ query +'", "data" : ['
	i = 0
	for item in list:
		i+=1
		need_output += '{ "title" : "'+item+'", "source" : "'+ facts_urls[list[item]] +'", "weight" : "'+ `weight[list[item]]` +'" }'
		if i != len(list):
			need_output += ', '	

	need_output += ']}'
	return need_output

#print(parser("/srv/http/app/facts/text"))