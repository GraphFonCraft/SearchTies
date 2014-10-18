from xml.dom import minidom
xmldoc = minidom.parse('items.xml')
itemlist1 = xmldoc.getElementsByTagName('Adj')
itemlist2 = xmldoc.getElementsByTagName('Noun')


for i in range(len(itemlist2)):
    print itemlist1[i].attributes['val'].value + " " + itemlist2[i].attributes['val'].value
