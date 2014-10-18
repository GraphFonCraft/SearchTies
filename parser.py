from xml.dom import minidom

def parser(xmlfile):
    xmldoc = minidom.parse(str(xmlfile))
    itemlist1 = xmldoc.getElementsByTagName('Adj')
    itemlist2 = xmldoc.getElementsByTagName('Noun')
    need_output = '{"id100" : {"source" : "http://" : [\n'
    for i in range(len(itemlist2)):
        if i!= (len(itemlist2)-1):
            need_output += '"' + itemlist1[i].attributes['val'].value + " " + itemlist2[i].attributes['val'].value + '",\n '
        else:
            need_output += '"' + itemlist1[i].attributes['val'].value + " " + itemlist2[i].attributes['val'].value + '"\n]}}'
    return need_output

print parser('items.xml')

