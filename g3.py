import codecs
from lxml import etree
from io import BytesIO,StringIO
fp=codecs.open("About this Documentation _ Node.js v8.9.4 Documentation.html","r","utf-8")
html=fp.read()
html = etree.HTML(html)
h1s=html.xpath("./body/div/div/div/h1/span/a")
#for h1 in h1s:
#	print(h1,h1.attrib["id"])
h2s=html.xpath("./body/div/div/ul/li/a")
for i in range(len(h1s)):
	print(h2s[i].attrib["href"])
	newv="#"+h1s[i].attrib["id"]
	h2s[i].attrib["href"]=newv
	print(h2s[i].attrib["href"])
	pass
print(dir(html))
s=BytesIO()
html.getroottree().write(s, encoding="utf-8", xml_declaration=False, method="html")	
f=open("out.html","wb")
s.seek(0)
f.write(s.read())
f.close()
