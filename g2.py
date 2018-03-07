from requests_html import HTML
import codecs
fp=codecs.open("About this Documentation _ Node.js v8.9.4 Documentation.html","r","utf-8")
html = HTML(html=fp.read())
# c2=html.find('#column2', first=True)
# print(c2,dir(c2))
h1s=html.xpath("./body/div/div/div/h1/span/a")
for h1 in h1s:
	print(h1.attrs["id"])
print(len(h1s))	
h2s=html.xpath("./body/div/div/ul/li/a")
for i in range(len(h1s)):
	print(h2s[i].attrs["href"])
	print("#"+h1s[i].attrs["id"])
	#print(h2s[i].attrs["href"])
	pass
