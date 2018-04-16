from bs4 import BeautifulSoup
import codecs
with codecs.open("About this Documentation _ Node.js v8.9.4 Documentation.html","r","utf-8") as fp:
    soup = BeautifulSoup(fp)
    column2=soup.find_all(id='column2')
    #print(len(body))
    #print(type(body),dir(body))
    #divs=body.find_all('div')
    #print(len(divs))